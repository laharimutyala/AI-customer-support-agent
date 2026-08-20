# AI Customer Support Agent

An AI-powered customer support application that helps process customer tickets through automated classification, AI-generated responses, and escalation detection.

## Features

* Customer support ticket submission
* Automatic ticket classification
* AI-powered response generation
* Escalation detection
* Ticket data storage
* Streamlit user interface
* FastAPI backend

## Tech Stack

* Python
* Streamlit
* FastAPI
* SQLAlchemy
* Google Gemini
* SQLite
* REST API
* Git & GitHub

## How It Works

```text
Customer
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
Ticket Classification
   ↓
AI Response Generation
   ↓
Escalation Detection
   ↓
Database Storage
   ↓
Response to Customer
```

## Project Structure

```text
AI-customer-support-agent/
│
├── services/
│   ├── ai_responder.py
│   ├── classifier.py
│   ├── escalator.py
│   ├── responder.py
│   └── ticket_service.py
│
├── database.py
├── frontend.py
├── main.py
├── models.py
├── schemas.py
├── requirements.txt
├── test_models.py
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/laharimutyala/AI-customer-support-agent.git
cd AI-customer-support-agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the AI API key

Create a `.env` file in the project folder and add your API key.

```env
GEMINI_API_KEY=your_api_key_here
```

**Do not upload your `.env` file to GitHub.**

### 5. Start the backend

```bash
uvicorn main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

### 6. Start the frontend

Open another Terminal window:

```bash
cd /Users/pavanmutyala/Desktop/Customer-support-agent
source venv/bin/activate
streamlit run frontend.py
```

The Streamlit application will open in your browser.

## Project Purpose

This project demonstrates how AI can be integrated with a web application to automate common customer-support tasks and manage support tickets through a structured workflow.

## Author

**Lahari Mutyala**

GitHub: https://github.com/laharimutyala
