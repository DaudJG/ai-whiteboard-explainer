# hello_image.py
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types

def main():
    client = genai.Client()

    prompt = "A simple diagram illustrating gradient descent: a ball rolling down a curve toward a minimum."

    response = client.models.generate_images(
        model="gemini-2.5-flash-image-preview",
        prompt=prompt,
    )

    img = response.images[0]
    with open("outputs/hello.png", "wb") as f:
        f.write(img.image_bytes)

    print("=== IMAGE SAVED TO outputs/hello.png ===")

if __name__ == "__main__":
    main()
