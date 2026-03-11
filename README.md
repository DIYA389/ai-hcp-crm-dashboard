# AI-Powered HCP CRM Dashboard

An AI-powered CRM dashboard for logging and analyzing Healthcare Professional (HCP) interactions.
The system uses **React, FastAPI, LangGraph, and Groq LLM** to automatically extract structured data from interaction notes and store them in a database.

---

## Project Overview

This application helps pharmaceutical representatives or sales teams log their interactions with healthcare professionals.

Instead of manually filling forms, the user can simply describe the interaction in natural language, and the AI assistant automatically extracts structured information such as:

* HCP Name
* Interaction Type
* Topics Discussed
* Sentiment
* Materials Shared
* Follow-up actions

The extracted data is automatically populated into the CRM form.

---

## Features

* AI-powered interaction extraction using LLM
* Automatic form filling
* Prompt history storage
* Modern dashboard UI with Glassmorphism design
* Sidebar navigation (Dashboard, Interactions, Prompt History, Analytics)
* REST API backend
* SQLite database storage

---

## Tech Stack

### Frontend

* React
* Redux Toolkit
* Axios
* CSS (Glassmorphism UI)

### Backend

* FastAPI
* LangGraph
* LangChain
* Groq LLM API

### Database

* SQLite
* SQLAlchemy ORM

---

## Project Structure

```
hcp-model/
│
├── backend/
│   ├── main.py
│   ├── langgraph_agent.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AIChat.js
│   │   │   ├── InteractionForm.js
│   │   │   └── Layout.js
│   │   │
│   │   ├── redux/
│   │   │   ├── store.js
│   │   │   └── interactionSlice.js
│   │   │
│   │   ├── App.js
│   │   └── App.css
│
└── README.md
```

---

## Installation Guide

### 1. Clone the Repository

```
git clone https://github.com/your-username/hcp-crm-ai.git
cd hcp-crm-ai
```

---

### 2. Backend Setup

Navigate to backend folder:

```
cd backend
```

Create virtual environment:

```
python -m venv .venv
```

Activate environment:

Windows

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run FastAPI server:

```
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

Navigate to frontend folder:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run React app:

```
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## API Endpoints

### Extract Interaction

```
POST /ai-extract
```

Example request:

```
{
  "prompt": "Met Dr Sharma at Apollo Hospital today for a meeting. Discussed diabetes drug Prodo-X. Doctor was positive. Shared brochure. Follow up in two weeks."
}
```

---

### Prompt History

```
GET /history
```

Returns all stored prompts from the database.

---

## Future Improvements

* Interaction history dashboard
* Analytics with charts
* Authentication system
* Deployment to cloud
* Reminder system for follow-ups

---

## Author

Diya Roy
Artificial Intelligence & Machine Learning Student

---

## License

This project is for educational and portfolio purposes.
