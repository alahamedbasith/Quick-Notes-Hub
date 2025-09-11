import gradio as gr

def add(a, b): return a+b
def multiply(a, b): return a*b

demo = gr.TabbedInterface(
    [
        gr.Interface(add, ["number", "number"], "number"),
        gr.Interface(multiply, ["number", "number"], "number"),
    ],
    ["Add", "Multiply"]
)

demo.launch()
