# AI Whiteboard Explainer

Generate and refine AI/ML technical explanations and (soon) diagrams using the Gemini API.  
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

5. **Run the minimal Gemini test**

```powershell
python .\hello_gemini.py
```

You should see a one-sentence explanation printed to the console.

6. **(Optional) Verify the environment key**

```powershell
python .\test_env.py
```

---


## Dependencies (current)

* `google-genai` — official Gemini Python SDK
* `python-dotenv` — load `GEMINI_API_KEY` from `.env`
* `pydantic` — structured parsing/validation
* `rich` — pretty CLI output (screenshots/demos)
* `pillow` — image I/O (for upcoming diagram/image features)

> These are declared in `pyproject.toml`. If you add new packages, prefer:
>
> ```powershell
> uv add <package>
> uv pip sync .\uv.lock
> ```

---




