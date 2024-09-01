import streamlit as st
import os
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt
from src.misc import Misc
from src.timestamp_formatter import TimestampFormatter
from src.copy_module_edit import ModuleEditor
from dotenv import load_dotenv
from st_copy_to_clipboard import st_copy_to_clipboard

class VideoSummarizer:
    def __init__(self):
        self.youtube_url = None
        self.video_id = None
        self.video_title = None
        self.video_transcript = None
        self.video_transcript_time = None
        self.summary = None
        self.time_stamps = None
        self.transcript = None
        self.model_name = None
        self.col1 = None
        self.col2 = None
        self.col3 = None
        self.model_env_checker = []
        load_dotenv()

    def get_youtube_info(self):
        self.youtube_url = st.text_input("Enter YouTube Video Link")

        if os.getenv("GOOGLE_GEMINI_API_KEY"):
            self.model_env_checker.append("Gemini") 
        if not self.model_env_checker:
            st.warning('Error while loading the API keys from environment.', icon="⚠️")

        with self.col2:
            if self.model_env_checker:
                with st.container():
                    self.model_name = st.selectbox(
                        'Select the model',
                        self.model_env_checker)

        if self.youtube_url:
            self.video_id = GetVideo.Id(self.youtube_url)
            if self.video_id is None:
                st.write("**Error**")
                st.image("https://i.imgur.com/KWFtgxB.png", use_column_width=True)
                st.stop()
            self.video_title = GetVideo.title(self.youtube_url)
            st.write(f"**{self.video_title}**")
            st.image(f"http://img.youtube.com/vi/{self.video_id}/0.jpg", use_column_width=True)

    def generate_summary(self):
        if st.button("Get Summary", key="summary"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            if self.model_name == "Gemini":
                self.summary = Model.google_gemini(transcript=self.video_transcript, prompt=Prompt.prompt1())
            st.markdown("## Summary:")
            st.write(self.summary)
            st_copy_to_clipboard(self.summary)

    def generate_time_stamps(self):
        if st.button("Get Timestamps", key="timestamps"):
            self.video_transcript_time = GetVideo.transcript_time(self.youtube_url)
            youtube_url_full = f"https://youtube.com/watch?v={self.video_id}"
            if self.model_name == "Gemini":
                self.time_stamps = Model.google_gemini(self.video_transcript_time, Prompt.prompt1(ID='timestamp'), extra=youtube_url_full)
            st.markdown("## Timestamps:")
            st.markdown(self.time_stamps)
            cp_text = TimestampFormatter.format(self.time_stamps)
            st_copy_to_clipboard(cp_text)

    def generate_transcript(self):
        if st.button("Get Transcript", key="transcript"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            self.transcript = self.video_transcript
            st.markdown("## Transcript:") 
            st.download_button(label="Download as text file", data=self.transcript, file_name=f"Transcript - {self.video_title}")
            st.write(self.transcript)
            st_copy_to_clipboard(self.transcript)

    def run(self):
        st.set_page_config(page_title="Video Summarization System", page_icon="chart_with_upwards_trend", layout="wide")
        st.title("Video Summarization System")

        st.markdown(
            """
            <style>
            body {
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: orange;
            }
            .stButton button {
                background-color: #007BFF;
                color: orange;
                border: none; 
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }
            .stButton button:hover {
                background-color: #0056b3;
            }
            .stMarkdown {
                color: orange;
            }
            .stRadio label {
                color: orange;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        editor = ModuleEditor('st_copy_to_clipboard')
        editor.modify_frontend_files()
        
        self.col1, self.col2, self.col3 = st.columns(3)

        with self.col1:
            self.get_youtube_info()

        ran_loader = Misc.loaderx()
        loader_message = ran_loader

        with self.col3:
            mode = st.radio(
                "What do you want to generate for this video?",
                [":rainbow[**Summary**]", ":rainbow[**Timestamps**]", "**Transcript**"],
                index=0
            )
            if mode == ":rainbow[**Summary**]":
                with st.spinner(loader_message):
                    self.generate_summary()

            elif mode == ":rainbow[**Timestamps**]":
                with st.spinner(loader_message):
                    self.generate_time_stamps()
            else:
                with st.spinner(loader_message):
                    self.generate_transcript()

        st.write(Misc.footer(), unsafe_allow_html=True)


if __name__ == "__main__":
    app = VideoSummarizer()
    app.run()
