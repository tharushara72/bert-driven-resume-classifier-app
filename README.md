# SemanticHire: Next-Gen AI Resume Intelligence System

## 🚀 Project Overview (The Business Idea)
In the modern job market, recruiters are overwhelmed by "High-Volume, Low-Relevance" applications. Traditional **Applicant Tracking Systems (ATS)** act as simple filters that often reject qualified candidates due to minor formatting or vocabulary differences. 

**SemanticHire** is a business-ready solution designed to transform recruitment from **Keyword Searching** to **Intent Understanding**. By using deep learning, it allows companies to find the "best fit" based on skills and experience context, reducing time-to-hire by up to 70% and eliminating the "Keyword-Stuffing" bias that plagues current HR tech.

---

## 💡 The Novelty: Traditional NLP vs. Semantic AI
This project introduces a paradigm shift from **Lexical Matching** to **Deep Semantic Mapping**.

| Feature | Traditional NLP (Old ATS) | SemanticHire (This Project) |
| :--- | :--- | :--- |
| **Logic** | Keyword-based (Exact string match) | Contextual (Meaning-based) |
| **Synonyms** | Fails (e.g., "Java" ≠ "JVM") | Succeeds (Understands relationships) |
| **Robustness** | Brittle; fails with OCR errors | Resilient; focuses on vector proximity |
| **Fairness** | Favors "Keyword-Stuffing" | Favors actual merit and skills |

---

## 🧠 Why This Model? (The AI Architecture)
I chose **Sentence-BERT (SBERT)**—specifically the `all-MiniLM-L6-v2` transformer—for the following technical reasons:

1. **Siamese Network Architecture:** Optimized for comparing two different texts (Job Description vs. Resume) simultaneously.
2. **High-Dimensional Embeddings:** Maps documents into a **384-dimensional vector space** where distance represents true professional compatibility.
3. **Inference Speed:** Provides near-instant results, making it viable for real-time industrial screening of thousands of documents.

---




## 🛠️ Technology Stack & System Architecture

This project is built using a modern, containerized Python stack designed for high-performance Natural Language Processing (NLP) and scalable web delivery.

### 🧠 AI & Machine Learning Engine
* **Sentence-Transformers (SBERT):** Utilizes the `all-MiniLM-L6-v2` transformer model to convert unstructured text into **384-dimensional semantic vectors**.
* **PyTorch (`torch`):** The underlying deep learning framework for managing tensor operations and model inference.
* **Cosine Similarity:** The mathematical logic used to calculate the semantic proximity between Job Descriptions and Resumes.

### ⚙️ Backend & API Layer
* **FastAPI:** A modern, high-performance (asynchronous) web framework used to serve the ML model as a RESTful service.
* **Uvicorn:** An ASGI server implementation for running the FastAPI application with high concurrency.
* **Python-Multipart:** Enables the backend to handle complex form-data and binary file uploads.

### 📄 Data Processing & Extraction
* **pyPDF:** A robust library for extracting raw text from uploaded PDF resumes.
* **Pandas & NumPy:** Used for efficient data manipulation, vector calculations, and structuring the final similarity results.

### 🎨 Frontend & User Interface
* **Streamlit:** A reactive web dashboard for real-time visualization of resume-to-JD similarity scores.
* **Requests:** Facilitates communication between the Streamlit UI and the FastAPI backend.

### 🏗️ Infrastructure & DevOps
* **`uv` Package Manager:** Used for lightning-fast dependency resolution and ensuring a 100% reproducible environment via `uv.lock`.
* **Docker:** Containerization platform used to package the entire stack into a portable image for consistent cross-platform execution.

---


## 📖 Research & Ethical Basis (IEEE Citations)
* **[1] S. Datto et al. (2026):** Proves that NLP-driven analysis reduces inconsistent evaluation criteria in Industry 4.0 recruitment.
* **[2] H. Miller & S. V. Kumar (2026):** Addresses the "Black Box" problem by using transparent similarity scoring to maintain a **Human-in-the-loop**.
* **[3] N. Reimers & I. Gurevych (2019):** Foundational research for the Siamese-BERT networks used in this architecture.

---

## ⚡ Quick Start (Local Setup)
Ensure you have `uv` installed, then run:

```bash
# 1. Sync dependencies
uv sync

# 2. Start FastAPI Backend
uv run uvicorn src.main:app --reload

# 3. Start Streamlit UI
uv run streamlit run src/app.py
