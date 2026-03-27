from sentence_transformers import SentenceTransformer, util

# Load a lightweight, fast BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, job_description):
    # Encode both into vectors
    resume_vec = model.encode(resume_text, convert_to_tensor=True)
    jd_vec = model.encode(job_description, convert_to_tensor=True)
    
    # Calculate Cosine Similarity (Score between 0 and 1)
    score = util.cos_sim(resume_vec, jd_vec)
    return round(float(score) * 100, 2)