import gradio as gr

def uppercase(text):
    return text.upper()

demo = gr.Interface(
    fn=uppercase,
    inputs="text",
    outputs="text",
    live=True
)

demo.launch()
