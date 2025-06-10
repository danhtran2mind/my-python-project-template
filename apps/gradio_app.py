import gradio as gr

def greet(name):
    return fHello, {name}!

interface = gr.Interface(fn=greet, inputs=text, outputs=text)
interface.launch()
