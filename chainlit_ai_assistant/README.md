
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


## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant
````

2. **Install dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file**

   Create a `.env` file in the root directory and add your Google Gemini API key:

   ```env
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

4. **Run the app**

   Start the Chainlit app:

   ```bash
   chainlit run main.py
   ```

5. **Access the Assistant**

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

