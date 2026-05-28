# Healthcare chatbot

        Healthcare Chatbot built with FastAPI + Streamlit + Python

        ## Overview

        Create a healthcare chatbot

        Audience: students, developers, founders, and operations teams

        ## Tech Stack

        FastAPI + Streamlit + Python

        ## Core Features

        - Conversational question input
- Context-aware answer panel
- Suggested follow-up prompts
- Session summary and notes

        ## Key Entities

        - conversation
- message
- topic
- advice

        ## Frontend Sections

        - Overview
- Primary Input
- Response Output
- Suggested Actions

        ## API Endpoints

        - `GET /`: Service status
- `GET /blueprint`: Project configuration
- `POST /run`: Generate a structured assistant reply

        ## Sample Inputs

        - What questions can I ask this assistant?
- Give me a quick summary for a first-time user.
- What should I do next based on this issue?

        ## Run Locally

        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt
        python -m uvicorn backend.main:app --reload
        ```

        In another terminal:

        ```bash
        streamlit run frontend/app.py
        ```

        ## API Quick Test

        ```bash
        curl -X POST http://127.0.0.1:8000/chat ^
          -H "Content-Type: application/json" ^
          -d "{\"message\": \"What questions can I ask this assistant?\"}"
        ```

        ## Project Structure

        ```text
        backend/     FastAPI app, routes, schemas, services, and JSON storage
        frontend/    Streamlit user interface
        shared/      Generated blueprint used by backend and frontend
        tests/       Basic API smoke tests
        ```
