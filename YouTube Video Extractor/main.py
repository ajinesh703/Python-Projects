from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def summarize_youtube(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t['text'] for t in transcript])
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

video_id = input("Enter YouTube Video ID: ")
print("Summary:", summarize_youtube(video_id))
