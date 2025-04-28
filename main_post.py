from tools.linkedin_poster import linkedin_post
from tools.summaries import load_summaries, format_articles_for_prompt, reset_posting_files
from llms.posting import model, system_prompt
from config.settings import profile_path, profile_name
import os

def generate_post(summaries):
    prompt_with_data = system_prompt + "\n\n" + format_articles_for_prompt(summaries)
    
    response = model.generate_content(
        prompt_with_data,
        generation_config={
            "temperature": 0.7,
            "top_p": 1,
            "max_output_tokens": 1200
        }
    )
    return response.text.strip()


if __name__ == "__main__":
    try:
        # Check if final_post.txt already has content
        if os.path.exists("final_post.txt"):
            with open("final_post.txt", "r", encoding="utf-8") as f:
                existing_content = f.read().strip()

            if existing_content:
                print("⚠️ Post already generated in final_post.txt. Skipping agent run.")
                linkedin_post(post_text=existing_content, profile_path=profile_path, profile_name=profile_name, dry_run=False, headless=True)
                # Optionally reset here too, if this was intentional
                reset_posting_files()
                exit(0)

        # If final_post.txt is empty, generate new content
        summaries = load_summaries()
        post_text = generate_post(summaries)
        print("\n✅ Generated LinkedIn Post:\n")
        # print(post_text)

        # Save to file
        with open("final_post.txt", "w", encoding="utf-8") as f:
            f.write(post_text)

        linkedin_post(post_text=post_text, profile_path=profile_path, profile_name=profile_name, dry_run=False, headless=True)
        reset_posting_files()

    except Exception as e:
        print(f"❌ Error: {e}")
