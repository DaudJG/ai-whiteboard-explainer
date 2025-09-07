"""
Generate both an image and a text explanation for a given ML concept
using the Gemini API and the prompt templates in prompts.py.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from PIL import Image
from io import BytesIO

from prompts import PROMPTS

def generate_explainer(concept: str):
    if concept not in PROMPTS:
        raise ValueError(f"Concept '{concept}' not found in PROMPTS.")

    prompt = PROMPTS[concept]
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=prompt,
    )

    os.makedirs("outputs", exist_ok=True)

    text_output = []
    image_saved = False

    for cand in response.candidates:
        for part in cand.content.parts:
            if part.text:
                text_output.append(part.text)
            elif part.inline_data:
                image = Image.open(BytesIO(part.inline_data.data))
                image_path = f"outputs/{concept}.png"
                image.save(image_path)
                print(f"Image saved to {image_path}")
                image_saved = True

    if text_output:
        text_path = f"outputs/{concept}.txt"
        with open(text_path, "w", encoding="utf-8") as f:
            f.write("\n".join(text_output))
        print(f"Text explanation saved to {text_path}")

    if not image_saved:
        print("No image found in response.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_from_prompt.py <concept>")
        print(f"Available concepts: {', '.join(PROMPTS.keys())}")
        sys.exit(1)

    concept = sys.argv[1]

    if concept not in PROMPTS:
        print(f"Concept '{concept} not found.")
        print(f"Available concepts: {', '.join(PROMPTS.keys())}")
        sys.exit(1)


    generate_explainer(concept)

if __name__ == "__main__":
    load_dotenv()
    main()