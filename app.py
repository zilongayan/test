import gradio as gr

def greet(name):
    return "Hello " + name + "!!3"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
