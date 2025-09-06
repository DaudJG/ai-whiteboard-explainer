from dotenv import load_dotenv
load_dotenv() 

from google import genai
from google.genai import types

def main():
    client = genai.Client()

    prompt = "Explain gradient descent to a beginner in one clear sentence."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
      
    )

    print("=== MODEL TEXT OUTPUT ===")
    print(response.text)

if __name__ == "__main__":
    main()
