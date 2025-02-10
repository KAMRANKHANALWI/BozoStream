# BozoStream: Streamlit-Based AI Chatbot

🚀 A lightweight and interactive AI-powered chatbot built with **Streamlit**, **LangChain**, and **Groq's Llama-3.3-70B** for natural language conversations with multi-session management.

---

## 📌 Overview

BozoBot is an AI chatbot designed for intuitive and real-time interactions. Using **LangChain**, it efficiently manages chat history, enabling context-aware responses across multiple conversations. The **Streamlit-based frontend** ensures a clean and interactive UI for seamless user engagement.

### 🎯 **Key Features**

✅ **LLM-Powered Chat** – Uses Groq's Llama-3.3-70B for AI-driven responses.
✅ **Multi-Session Support** – Allows users to maintain multiple chats with historical context.
✅ **Context-Aware Responses** – Utilizes LangChain to track and process conversation history.
✅ **Streamlit UI** – Simple, clean, and responsive chat interface.
✅ **API Key Integration** – Securely loads API credentials using dotenv.
✅ **Low-Latency Inference** – Optimized for real-time responses with efficient query processing.

---

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/bozobot-streamlit.git
cd bozobot-streamlit
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and add your **Groq API Key**:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ Run the Chatbot

```bash
streamlit run main.py
```

- **Local URL:** `http://localhost:8501/`

---

## 📌 Key Functionalities & How It Works

### 🔹 **Conversation Management with LangChain**

- **Tracks Chat History:** Stores conversation logs in `st.session_state`.
- **Multi-Session Chats:** Allows users to create and switch between multiple conversations.
- **Context-Aware Responses:** Maintains relevant conversation context for improved AI responses.

### 🔹 **Real-Time Chat with Streamlit**

- Displays chat messages in a user-friendly format with custom UI styles.
- Automatically updates the interface as new messages are sent.
- Supports dynamic input handling and chatbot responses.

### 🔹 **Efficient API Interaction**

- Uses `ChatGroq` from LangChain for seamless integration with **Groq's Llama-3.3-70B**.
- Sends structured user queries and retrieves AI-generated responses.
- Limits chat context to the last 10 exchanges for optimal inference performance.

### 🔹 **Session Persistence**

- Saves user conversations in **Streamlit’s session state**.
- Enables smooth transitions between multiple chat sessions without losing history.
- Normalizes chat roles to align with LangChain’s expected format.

---

## 🚀 Deployment Guide

### **Deploy with Docker**

1. Create a `Dockerfile` in the project directory:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Build and Run:

```bash
docker build -t bozobot .
docker run -p 8501:8501 bozobot
```

### **Deploy on Streamlit Cloud**

1. Push your project to **GitHub**.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub repo and deploy the app.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** LangChain, FastAPI (for future expansions)
- **AI Model:** Groq Llama-3.3-70B
- **State Management:** Streamlit Session State
- **Hosting:** Streamlit Cloud, Docker (optional)

---

## 💡 Contributing

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify it!

---

## ✨ Acknowledgments

- **Streamlit** for the frontend framework.
- **LangChain** for seamless LLM integration.
- **Groq AI** for powering chatbot responses.

🚀 **Build AI-powered chat apps effortlessly with Streamlit & LangChain!**
