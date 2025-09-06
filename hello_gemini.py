from dotenv import load_dotenv
load_dotenv() 

from google import genai
from google.genai import types

def main():
    client = genai.Client()

    prompt = "Explain gradient descent to a beginner in one clear sentence."

    # NOTE: 2.5 Flash has 'thinking' on by default (higher quality, slower).
    # You can disable it via thinking_budget=0 to reduce latency/cost.
    # We'll keep defaults for now.
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        # config=types.GenerateContentConfig(
        #     thinking_config=types.ThinkingConfig(thinking_budget=0)
        # ),
    )

    print("=== MODEL TEXT OUTPUT ===")
    print(response.text)

if __name__ == "__main__":
    main()
