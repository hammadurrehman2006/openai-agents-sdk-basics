
# 🤖 Hammad ur Rehman's AI Assistant

Welcome to **Hammad ur Rehman's AI Assistant**, an intelligent conversational app powered by Google Gemini via the OpenAI-compatible API. This assistant is designed to provide helpful, context-aware responses in a chat interface using Chainlit.

## 🚀 Features

- ✅ Seamless chat experience with real-time typing indicators
- 🧠 Context-aware conversations with chat history memory
- 🔗 Integrated with **Google Gemini (v2.0-flash)** via OpenAI-compatible API
- 🛠️ Built using **Chainlit** for easy frontend management
- 🔐 Environment variable support using `.env` for secure API key management

## 📦 Tech Stack

- **Chainlit** – Chat app framework
- **Python** – Core language
- **Google Gemini API** – Powered by `generativelanguage.googleapis.com`
- **OpenAI-Compatible Wrapper** – Enables Gemini use via OpenAI-style client
- **dotenv** – For environment variable management

## 📁 Project Structure
.
├── agents/
│   └── run.py         # Contains agent runner and config logic
├── main.py            # Main app entry with Chainlit event handlers
├── .env               # Contains GEMINI\_API\_KEY
└── README.md

## Setup and Run with `uv`

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver, written in Rust.

1.  **Check for `uv` Installation**:
    Open your terminal and type `uv --version`. If it's installed, you'll see the version number. Otherwise, you need to install it.

2.  **Install `uv`** (if not already installed):
    You can install `uv` using pip, or by following the instructions on the [official `uv` installation guide](https://github.com/astral-sh/uv#installation).
    ```bash
    # Example using pip (ensure pip is available)
    pip install uv
    ```

3.  **Clone the Repository (if you haven't already)**:
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd chainlit_ai_assistant
    ```

4.  **Navigate to the Project Directory**:
    Ensure you are in the `chainlit_ai_assistant` directory. (This step might be redundant if you just cloned and cd'd).

5.  **Set up your `.env` file**:
    Create a `.env` file in the project root by copying the example and add your Google Gemini API key:
    ```bash
    cp .env.example .env
    # Now edit .env and add your GEMINI_API_KEY
    ```
    The `.env` file should look like this:
    ```env
    GEMINI_API_KEY=your_google_gemini_api_key
    ```

6.  **Create a Virtual Environment and Install Dependencies**:
    `uv` will create a virtual environment in the `.venv` directory and install dependencies from the `requirements.txt` file (as this project uses it, and `uv.lock` if present).
    ```bash
    uv venv  # Create the virtual environment
    uv sync  # Install dependencies from requirements.txt (or uv.lock)
    ```
    If you prefer to activate the virtual environment explicitly before syncing (optional):
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    # For Windows (Command Prompt): .venv\Scripts\activate.bat
    # For Windows (PowerShell): .venv\Scripts\Activate.ps1
    uv sync
    ```
    *Note: This project uses a `requirements.txt` file. `uv sync` will use this file to install dependencies if a `pyproject.toml` is not present or not configured for project dependencies.*

7.  **Run the App with `uv`**:
    Once the dependencies are installed (and the virtual environment is active, if you activated it manually), run the Chainlit app using `uv`.
    ```bash
    uv run chainlit run main.py
    ```

8. **Access the Assistant**:
   Visit [http://localhost:8000](http://localhost:8000) in your browser.

## 💡 How It Works

* When a user starts the chat, the app initializes a Gemini-powered agent.
* Messages are processed using a custom `Agent` and `Runner`.
* Chat context is preserved within a session using `cl.user_session`.
* The agent responds intelligently based on previous inputs.

## 📷 Screenshots

*(Include screenshots of your app interface here if available)*

## 🛡️ Security

Make sure to **never commit your `.env` file** or expose your API keys. Use `.gitignore` to exclude sensitive files.

## 📜 License

MIT License. Feel free to use and modify this project.

---

Made with ❤️ by **Hammad ur Rehman**

