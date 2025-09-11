import gradio as gr
from PIL import ImageOps

def invert_colors(img):
    return ImageOps.invert(img)

demo = gr.Interface(
    fn=invert_colors,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil")
)

demo.launch()
