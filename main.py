import gradio as gr
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import re

def islinkcompatible (link):
    #TODO: complete function
    return()

def transcriptvideo (link):
    #TODO: complete function
    return()

def exporttranscription(link):
    #TODO: complete function
    return ()

def input(link):
    istheinputtextayoutubelink=re.findall('youtu',link)
    if istheinputtextayoutubelink:
        link=YouTube(link).streams.filter(only_audio=True).get_highest_resolution
        subtitles = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")
        print(subtitles)
        return {"output_text":subtitles, "output_text":gr.update(visible=True)}
    else:
        print("not a youtube link")
        return{"output_text": "The link is not a youtube link","output_text":gr.update(visible=True)}

with gr.Blocks(css="#button {width:200px;}") as demo:
    #TODO: adjusting button size in CSS
    with gr.Row():
        link = gr.Textbox(placeholder="Collez votre lien Youtube ici",max_lines=1, show_label=False)
        input_btn = gr.Button("Générer", elem_id="button")
    output_text = gr.Textbox(max_lines=1, show_label=False, visible=False)
    input_btn.click(fn=input, inputs=link, outputs=output_text)

demo.launch()
