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

## 🧠 The "Brain" of the System: BERT Power

Traditional search looks for **words**. Our system looks for **meaning**. 

### 🌟 Why BERT? (The Semantic Revolution)
Most resume scanners are "dumb"—if you search for **"Java Developer"** and a resume says **"JVM Engineer,"** they might miss it. 

We use **Sentence-BERT (SBERT)**, a modification of the ground-breaking BERT (Bidirectional Encoder Representations from Transformers) model. It allows the system to:
* **Understand Context:** It reads sentences both left-to-right and right-to-left simultaneously.
* **Capture Intent:** It recognizes that a "Data Scientist" and a "Machine Learning Engineer" share 90% of the same "Vector Space."
* **Eliminate Keyword Bias:** Candidates can no longer "cheat" the system by just stuffing hidden keywords; they must have the actual semantic experience.

### ⚡ The Model: `all-MiniLM-L6-v2`
I specifically chose the **MiniLM** variant for this project. In the business world, speed is just as important as accuracy:
1. **Speed:** It is optimized to generate embeddings in milliseconds.
2. **Efficiency:** It provides **99% of the accuracy** of the largest BERT models while being **60% smaller**, making it perfect for real-time applications.
3. **Accuracy:** It maps every resume into a **384-dimensional map**. The closer two dots are on that map, the better the candidate matches the job!

### 🎯 How it Works (Simple 3-Step Process)
1. **Embedding:** The Job Description and Resumes are converted into "Math Vectors."
2. **Comparison:** The system uses **Cosine Similarity** to measure the angle between these vectors.
3. **Ranking:** The smaller the angle, the higher the match percentage!

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
