import gradio as gr
from pytube import YouTube
from pytube import extract
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import re

def is_the_input_text_a_youtube_link(link):
    if re.findall('youtu',link):
        link=YouTube(link).streams.filter(only_audio=True).get_highest_resolution
        print("is_the_input_text_a_youtube_link(link) ")
        return()
    else:
        print("this link is not a youtube link")

def get_youtube_id(link):
    video_id=extract.video_id(link)
    print("the video id is"+video_id)
    return(video_id)

def get_subtitles_from_video (link):
    subtitles = YouTubeTranscriptApi.get_transcript(get_youtube_id(link))
    print(subtitles)
    return(subtitles)

def formatting_csv(link):
    df=pd.DataFrame(get_subtitles_from_video(link))
    video_names_list=[]
    value=""
    for i in range (len(df)):
        video_names_list.append("video_part_"+str(i))
    df.insert(0,"video name",video_names_list)
    print(df)
    return()

def export_subtitles_and_audio(link):
    #TODO: exporting archive with csv file and multiple audio files in it
    return ()

def input(link):
    is_the_input_text_a_youtube_link(link)
    formatting_csv(link)



with gr.Blocks(css="#button {width:200px;}") as demo:
    #TODO: adjusting button size in CSS
    with gr.Row():
        link = gr.Textbox(placeholder="Collez votre lien Youtube ici",max_lines=1, show_label=False)
        input_btn = gr.Button("Générer", elem_id="button")
    output_text = gr.Textbox(placeholder="Le résumé de votre vidéo ici",max_lines=1, show_label=False)
    input_btn.click(fn=input, inputs=link, outputs=output_text)

demo.launch()
