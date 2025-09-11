import gradio as gr
from transformers import pipeline

# pip install transformers
# pip install torch

# Load pretrained model
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    return f"Label: {result['label']} | Score: {result['score']:.2f}"

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter a sentence..."),
    outputs="text"
)

demo.launch()
