import gradio as gd

# def greet(name):
#     return f"Welcome {name}"

# demo = gd.Interface(
#     fn = greet,
#     inputs= "text",
#     outputs= "text"
# )
# # greet("Ahamed")

# demo.launch()

# Multiple Inputs

import gradio as gr

def calculate(name, age):
    return f"Hello {name} Your age doubled is {age*2}"

demo = gr.Interface(
    fn=calculate,
    inputs=["text", "number"],
    outputs=["text"]
)

demo.launch()
