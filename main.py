
from fastapi import FastAPI, File, UploadFile
import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MOONDREAM_API_KEY")

app = FastAPI()
@app.get("/health")
async def root():
    return {"status": "ok", "model": "moondream3"}
@app.get("/classes")
async def get_classes():
    return {"classes": ["biryani", "gulab jamun", "seekh kebab"]}

stats = {"total_predictions": 0,
     "class_counts": {
    "biryani": 0,
    "gulab_jamun": 0,
    "seekh_kebab": 0
  }
  }
@app.get("/stats")
async def get_stats():
    return (stats)



# ✅ Constants here, outside everything
CHECKPOINT_ID = "01KWVHDGSG3H40D9QDH9BY4A1T"
QUESTION = "Is this biryani, gulab jamun, or seekh kebab? Answer with only the food name."
CLASS_KEYWORDS = {
    "biryani": ["biryani"],
    "gulab_jamun": ["gulab jamun", "gulab-jamun"],
    "seekh_kebab": ["seekh kebab", "seekh kabab"],
}

def predict_food(image_bytes):          
    img_base64 = base64.b64encode(image_bytes).decode()
 
    response = requests.post(
        "https://api.moondream.ai/v1/query",
        headers={
            "X-Moondream-Auth": API_KEY,
            "Content-Type": "application/json",
        },
        json={
            "image_url": f"data:image/jpeg;base64,{img_base64}",
            "question": QUESTION,
            "model_id": CHECKPOINT_ID,
        },
        timeout=30
    )

    if response.status_code == 200:
        answer = response.json().get("answer", "").lower().strip()

        # Match to class
        for cls, keywords in CLASS_KEYWORDS.items():
            if any(kw in answer for kw in keywords):
                return cls, answer

        return "unknown", answer
    else:
        raise Exception(f"API error: {response.status_code} {response.text[:100]}")

@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    image_bytes = await file.read()
    food_prediction, answer = predict_food(image_bytes)
    stats["total_predictions"] += 1
    if food_prediction in stats["class_counts"]:
        stats["class_counts"][food_prediction] += 1
    return {"predicted_class": food_prediction, "raw_answer": answer, "status": "success", "warning": "This model only recognizes biryani, gulab jamun, and seekh kebab."} 

