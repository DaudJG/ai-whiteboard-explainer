here’s a **clean, updated README.md** you can copy-paste directly — includes the corrected image-generation notes so future readers don’t fall into the `.images[0]` trap.

````markdown
# AI Whiteboard Explainer

Generate and refine AI/ML technical explanations and diagrams using the Gemini API.  
Built for education, technical content, and AI/ML learning.

---

## Prerequisites

- Windows 10
- Python **3.11+**
- **uv** (fast Python packaging & virtualenvs)
  - Install uv (PowerShell):
    ```powershell
    irm https://astral.sh/uv/install.ps1 | iex
    ```
  - If scripts are blocked:
    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

---

## Quickstart

1) **Clone the repo**
```powershell
git clone https://github.com/DaudJG/ai-whiteboard-explainer.git
cd ai-whiteboard-explainer
````

2. **Create & activate a virtual environment (Windows PowerShell)**

```powershell
uv venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Install dependencies**

* If you want **exact pinned versions** (recommended):

  ```powershell
  uv pip sync .\uv.lock
  ```
* If you prefer to resolve from the project file:

  ```powershell
  uv pip sync .\pyproject.toml
  ```

4. **Add your Gemini API key**

* Copy the example env file and set your key:

  ```powershell
  copy .env.example .env
  ```

  Open `.env` and set:

  ```
  GEMINI_API_KEY=your_real_key_here
  ```

5. **Run the minimal Gemini text test**

```powershell
python .\hello_gemini.py
```

You should see a one-sentence explanation printed to the console.

6. **List available models (sanity check)**

```powershell
python .\list_models.py
```

This prints all models available to your API key (including `gemini-2.5-flash-image-preview`).

7. **Run the image generation example**

```powershell
python .\hello_image.py
```

The script will:

* Call the **`gemini-2.5-flash-image-preview`** model
* Loop through `response.candidates[0].content.parts`
* Save the first `inline_data` image to `outputs/hello.png`

 **Important:** The SDK does *not* return `response.images`. Images always appear as `inline_data` parts in the response. This is why the early attempt failed.

8. **(Optional) Verify the environment key**

```powershell
python .\test_env.py
```

---

## Dependencies (sample)

* `google-genai` — official Gemini Python SDK
* `python-dotenv` — load `GEMINI_API_KEY` from `.env`
* `pydantic` — structured parsing/validation
* `pillow` — image I/O (for diagram/image features)

> These are declared in `pyproject.toml`. If you add new packages, prefer:
>
> ```powershell
> uv add <package>
> uv pip sync .\uv.lock
> ```

---