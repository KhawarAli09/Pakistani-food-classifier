
import streamlit as st
import requests
import base64
from PIL import Image
import io

# ============================================================================
# CONFIG
# ============================================================================
import streamlit as st
API_KEY = st.secrets["MOONDREAM_API_KEY"]
CHECKPOINT_ID = "01KWVHDGSG3H40D9QDH9BY4A1T"
QUESTION = "Is this biryani, gulab jamun, or seekh kebab? Answer with only the food name."

CLASS_KEYWORDS = {
    "biryani": ["biryani"],
    "gulab jamun": ["gulab jamun", "gulab-jamun"],
    "seekh kebab": ["seekh kebab", "seekh kabab"],
}

CLASS_DESCRIPTIONS = {
    "biryani": "A fragrant Pakistani rice dish cooked with spices and meat.",
    "gulab jamun": "A popular Pakistani sweet made of milk solids soaked in sugar syrup.",
    "seekh kebab": "Spiced minced meat grilled on skewers, a Pakistani street food staple.",
    "unknown": "This dish was not recognized as biryani, gulab jamun, or seekh kebab.",
}

# ============================================================================
# INFERENCE
# ============================================================================
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
        for cls, keywords in CLASS_KEYWORDS.items():
            if any(kw in answer for kw in keywords):
                return cls, answer
        return "unknown", answer
    else:
        raise Exception(f"API error: {response.status_code}")

# ============================================================================
# UI
# ============================================================================
st.set_page_config(
    page_title="Pakistani Food Classifier",
    page_icon="🍛",
    layout="centered"
)

st.title("🍛 Pakistani Food Classifier")
st.markdown("Upload a photo of **biryani**, **gulab jamun**, or **seekh kebab** to identify it.")
st.warning("⚠️ This model recognizes 3 Pakistani food classes only. Other foods will be misclassified.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Predict
    with st.spinner("Identifying food..."):
        try:
            # Convert to JPEG bytes
            img_buffer = io.BytesIO()
            image.convert("RGB").save(img_buffer, format="JPEG")
            img_bytes = img_buffer.getvalue()
            
            predicted_class, raw_answer = predict_food(img_bytes)
            
            # Show result
            st.markdown("---")
            if predicted_class != "unknown":
                st.success(f"✅ **{predicted_class.upper()}**")
            else:
                st.error("❌ **UNKNOWN FOOD**")
            
            st.markdown(f"**Description:** {CLASS_DESCRIPTIONS[predicted_class]}")
            st.markdown(f"**Model answer:** *{raw_answer}*")
            
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown(
    "Built with [Moondream3](https://moondream.ai) · "
    "Fine-tuned on 87 Pakistani food images · "
    "94.4% accuracy on held-out test set"
)
