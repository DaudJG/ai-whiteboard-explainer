from dotenv import load_dotenv
load_dotenv()

from google import genai

def main():
    client = genai.Client()
    print("=== AVAILABLE MODELS ===")
    for m in client.models.list():
        print(m.name)

if __name__ == "__main__":
    main()
