import gradio as gr
from pytube import YouTube

#TODO: filling input function with youtube link recogntion, else return error
def input(input_text):
    input_text=YouTube(input_text)
    return {output_text:input_text.streams.filter(only_audio=True).get_highest_resolution}

with gr.Blocks(css="#button {width:200px;}") as demo:
    #TODO: adjusting button size in CSS
    with gr.Row():
        input_text = gr.Textbox(placeholder="Collez votre lien Youtube ici",max_lines=1, show_label=False)
        input_btn = gr.Button("Générer", elem_id="button")
    output_text = gr.Textbox(visible=True, max_lines=1, show_label=False)
    input_btn.click(fn=input, inputs=input_text, outputs=output_text)
 
demo.launch()
