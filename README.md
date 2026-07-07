# Pakistani Food Classifier using Moondream3

A Vision-Language Model (VLM) application that classifies images of Pakistani dishes into three categories: **Seekh Kebab**, **Gulab Jamun**, and **Biryani**.

## 🎯 Project Overview

This project demonstrates the practical application of Vision-Language Models (VLMs) for food image classification. Using Moondream3's powerful vision capabilities, the app can identify Pakistani dishes from user-uploaded images through natural language prompting.

## 📊 Model Performance

- **Overall Accuracy**: 94.4%
- **Dataset Size**: 120+ images across 3 classes
- **Model**: Moondream3 (via API)
- **Classification Approach**: Moondream3 VLM with structured prompting

### Class-wise Performance
- Seekh Kebab: ~96% accuracy
- Biryani: ~95% accuracy  
- Gulab Jamun: ~93% accuracy (occasional misclassification with seekh kebab ~7% failure rate)

## 🚀 Live Demo

**Try it here**: https://vlm-pakistani-food-classifier-09.streamlit.app/


## ✨ Features

- **Real-time Image Classification**: Upload an image and get instant predictions
- **VLM-Powered**: Uses state-of-the-art vision-language modeling
- **User-Friendly Interface**: Clean Streamlit UI with example images
- **Confidence Scores**: Displays prediction confidence for transparency
- **Batch Processing**: Upload multiple images for classification

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Vision Model**: Moondream3 (VLM)
- **Backend**: Python
- **API**: Moondream API
- **Deployment**: Streamlit Cloud

## 📦 Installation

### Prerequisites
- Python 3.8+
- Moondream API key (get it from [Moondream.ai](https://moondream.ai))

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/KhawarAli09/pakistani-food-classifier.git
cd pakistani-food-classifier
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.streamlit/secrets.toml` file in the project root:
```toml
MOONDREAM_API_KEY = "your-api-key-here"
```

4. **Run the application**
```bash
streamlit run app.py
```


## 📝 Usage

1. **Launch the app** using the instructions above
2. **Upload an image** of a Pakistani dish (seekh kebab, gulab jamun, or biryani)
3. **View the prediction** along with confidence score
4. **Try with multiple images** to test the model's performance

## 🔍 How It Works

The application uses a structured prompting approach with Moondream3:

1. **Image Input**: User uploads a food image
2. **VLM Processing**: Moondream3 analyzes the image using vision capabilities
3. **Structured Prompt**: The model is asked to classify the image into one of three categories
4. **Response Parsing**: The app parses the VLM's response and displays the prediction
5. **Confidence Score**: Extracts confidence information from the model's reasoning

## 📂 Project Structure

```
pakistani-food-classifier/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .streamlit/
│   └── secrets.toml      # API keys (not tracked by git)
└── sample_images/        # Sample images for testing
    ├── seekh_kebab.jpg
    ├── gulab_jamun.jpg
    └── biryani.jpg
```

## ⚠️ Known Limitations

- **Closed-set Classification**: The model can only classify images into the three trained categories. Unknown foods will be forced into one of these classes.
- **Gulab Jamun Misclassification**: Approximately 7% of gulab jamun images may be misclassified as seekh kebab due to similar color/texture profiles in certain lighting conditions.
- **Dataset Size**: The current dataset (120+ images) is relatively small. Expanding the dataset would improve accuracy and robustness.
- **Excluded Dishes**: Karahi and Nihari were excluded from the current version due to visual ambiguity with other classes at this dataset size.


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Dataset Contributions

If you have high-quality images of Pakistani dishes, please consider contributing to the dataset. Ensure you have the right to share the images.

## 🙏 Acknowledgments

- **Moondream.ai** for providing the Vision-Language Model API
- **Streamlit** for the excellent web app framework
- **Pakistani food enthusiasts** who contributed to dataset collection

## 📧 Contact

**Khawar Ali**  
GitHub: [@KhawarAli09](https://github.com/KhawarAli09)  
Project Link: [https://github.com/KhawarAli09/pakistani-food-classifier](https://github.com/KhawarAli09/pakistani-food-classifier)


---

**Built with ❤️ for Pakistani food lovers and AI enthusiasts**
