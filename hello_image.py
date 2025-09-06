from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

def main():
    client = genai.Client()

    prompt = "A simple diagram illustrating gradient descent: a ball rolling down a curve toward a minimum."

    response = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=prompt,
    )

    os.makedirs("outputs", exist_ok=True)

    for cand in response.candidates:
        for part in cand.content.parts:
            if part.text is not None:
                print("MODEL TEXT OUTPUT:", part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image.save("outputs/hello.png")
                print("=== IMAGE SAVED TO outputs/hello.png ===")
                return

if __name__ == "__main__":
    main()
