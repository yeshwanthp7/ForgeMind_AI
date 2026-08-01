from ocr import extract_text_from_image
from pdf_parser import extract_pdf_text
from csv_parser import read_csv
from risk import calculate_risk
from root_cause import find_root_cause
from recommendation import recommend
from rag import search_rag

# Add this function here
def analyze_incident(data):
    machine_data = {
        "temperature": data.get("temperature", 120),
        "pressure": data.get("pressure", 160),
        "vibration": data.get("vibration", 9)
    }

    score, level = calculate_risk(machine_data)
    cause = find_root_cause(level, "Machine temperature is increasing and overheating")
    actions = recommend(cause, level)

    return {
        "risk_score": score,
        "risk_level": level,
        "root_cause": cause,
        "recommendations": actions
    }

print("===== ForgeMind AI =====")

# OCR
image_text = extract_text_from_image("sample_data/sample_image.png")
print("\nOCR Output:")
print(image_text)

# PDF
pdf_text = extract_pdf_text("sample_data/sample_report.pdf")
print("\nPDF Output:")
print(pdf_text)

# CSV
csv_data = read_csv("sample_data/sample_log.csv")
print("\nCSV Output:")
print(csv_data)

knowledge = f"""
{image_text}

{pdf_text}

{csv_data.to_string()}
"""

print("\nKnowledge Base:")
print(knowledge)

# ================= CHUNKING + EMBEDDING =================

from embeddings import create_chunks, create_embeddings

# Chunking
chunks = create_chunks(knowledge)

# Embedding + FAISS
model, index, embeddings = create_embeddings(chunks)

query = "Why is the machine overheating?"
result = search_rag(query)

print("\nRAG Search:")
print("User Query:", query)
print("Relevant Knowledge:", result)

# Risk Analysis
machine_data = {
    "temperature": 120,
    "pressure": 160,
    "vibration": 9
}

score, level = calculate_risk(machine_data)

print("\nRisk Score:", score)
print("Risk Level:", level)

# Root Cause
incident = "Machine temperature is increasing and overheating"
cause = find_root_cause(level, incident)

print("\nRoot Cause:")
print(cause)

# Recommendation
actions = recommend(cause, level)

print("\nRecommended Actions:")
for action in actions:
    print("-", action)