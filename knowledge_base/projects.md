# Projects — Mohammad Awez Haider

## 1. Aquelious — Aquaculture Monitoring & Alert System
**Organization:** Aquelious (Startup)
**Role:** Technical Lead
**Status:** Active, in development

### Problem
Aquaculture farmers have no reliable way to monitor water quality parameters in real time. Harmful changes in dissolved oxygen, pH, temperature, or turbidity can kill entire fish populations before the farmer even notices. The goal is to detect these anomalies early and alert farmers before damage occurs — and eventually predict harmful conditions before they happen.

### What I Built
- End-to-end signal processing pipeline for raw sensor telemetry data
- Noise filtering using moving average, median, Gaussian, Butterworth, and Kalman filter techniques
- Anomaly detection system using lag-based difference analysis and z-score methods with flag persistence logic
- EDA (Exploratory Data Analysis) on water quality telemetry — identifying patterns, drift, and sensor noise
- ML-based predictive modeling for early warning alerts (in progress)
- Led sprint planning and technical documentation for a team of 4 engineers

### Tech Stack
- Python, Pandas, NumPy, SciPy
- Signal processing libraries
- Machine Learning (Scikit-learn)
- Custom anomaly detection logic

### Impact
Farmers receive real-time alerts when water quality parameters enter dangerous thresholds. Future versions will predict harmful conditions in advance, giving farmers time to take precautionary action before any fish are lost.

---

## 2. Tata Steel — Machine Performance Dashboard & RAG Chatbot
**Organization:** Tata Steel, SNTI Institute (Tata Prashikshan)
**Role:** Summer Intern
**Status:** Completed

### Problem
Tracking machine performance across shifts and machine types in a steel plant is complex and time-consuming. Engineers needed a faster way to analyze deviations, identify underperforming machines, and extract insights from internal documents without reading through everything manually.

### What I Built
- Power BI dashboard connected to PostgreSQL covering machine-wise performance metrics, shift-wise analysis, deviation tracking, and gas cutting analytics
- Python data loader script to ingest CSV machine monitoring data into PostgreSQL
- RAG-powered internal chatbot using LangChain, FAISS, and Groq LLM — enabling engineers to query internal documents and get instant, accurate answers

### Tech Stack
- Power BI, PostgreSQL
- Python, LangChain, FAISS, Groq
- Django (for chatbot backend)

### Impact
Reduced time spent manually tracking machine performance. Engineers can now query internal knowledge instantly through the chatbot instead of searching through documents.

---

## 3. RON — Personal AI Portfolio Chatbot
**Organization:** Personal Project
**Role:** Solo Developer
**Status:** Active, in development

### Problem
A static portfolio website tells recruiters what you've done — but it can't answer follow-up questions, explain projects in depth, or respond to recruiter queries at 2am. RON solves this.

### What I Built
- Full RAG pipeline from scratch using LangChain, FAISS, and Groq
- Django + DRF backend serving RON as an API endpoint
- Knowledge base of personal documents (bio, resume, projects) that RON uses to answer questions accurately
- Deployed on Railway with Docker containerization
- CI/CD pipeline via GitHub Actions

### Tech Stack
- Python, Django, Django REST Framework
- LangChain, FAISS, Groq
- Docker, GitHub Actions, Railway

### Purpose
Built to deeply understand RAG architecture by implementing it end to end — not from a tutorial, but from first principles. RON is both a portfolio feature and a proof of capability.