# 💔 HeartMend

**HeartMend** is an AI-powered breakup recovery web app that helps users heal emotionally through empathetic conversations, honest insights, and personalized recovery routines.

Built using a **multi-agent AI system**, HeartMend analyzes user emotions (text + optional chat screenshots) and provides structured emotional support in a calm, human-friendly way.

---

## ✨ Features

- 🤗 **Emotional Support Agent**
  - Validates feelings with empathy
  - Provides comforting, supportive responses

- ✍️ **Closure Agent**
  - Helps express unsent emotions
  - Generates closure messages and rituals

- 📅 **Recovery Planner Agent**
  - Creates a personalized 7-day healing plan
  - Suggests self-care, routines, and activities

- 💪 **Brutal Honesty Agent**
  - Gives direct, objective feedback
  - Encourages growth and moving forward

- 🖼️ **Image + Text Understanding**
  - Accepts chat screenshots to better understand emotional context

- 🌐 **Mobile-Friendly Web App**
  - Built with Streamlit
  - Clean, minimal, distraction-free UI

---

## 🧠 How It Works

1. User shares their feelings (text input)
2. Optional chat screenshots are uploaded
3. Images are processed and passed to AI agents
4. Multiple agents collaborate to provide:
   - Emotional support
   - Closure guidance
   - Recovery plan
   - Honest perspective

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **AI Framework**: Agno (multi-agent system)
- **LLM Provider**: OpenRouter
- **Vision Support**: Agno Image inputs
- **Tools**: DuckDuckGo (for factual context)
- **Environment Management**: python-dotenv

---

## 📂 Project Structure

heartmend/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .env


---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here


▶️ Running the App
1. Install dependencies
pip install -r requirements.txt

2. Run Streamlit app
streamlit run app.py

⚠️ Disclaimer

HeartMend is not a replacement for professional mental health care.
It is intended as a supportive, reflective tool for emotional processing and personal growth.

🌱 Future Improvements

Push notifications & reminders

Persistent user history

Mood tracking & analytics

PWA support

Database integration (Supabase)

❤️ Philosophy

Healing takes time.
HeartMend is here to walk with you — one step at a time.

📜 License

MIT License

