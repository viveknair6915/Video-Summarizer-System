<h1 align="center">
  <br>
   🎥 Video Summarizer System
  <br>
</h1>

<h4 align="center">Making world simpler</h4>


<p align="center">
  <a href="#overview-">Overview</a> •
  <a href="#features-">Features</a> •
  <a href="#getting-started-">Getting Started</a> •
</p>

## Overview 📝

The Video Summarizer System is a Python-based application designed to generate concise summaries of videos using machine learning techniques. It integrates components like video transcription and summarization to produce streamlined video content.


## Features ✨

- Automatic extraction of key insights and timestamps from YouTube videos.
- Utilizes youtube-transcript-api for getting the transcripts/subtitles YouTube video.
- Option for users to select AI models like *Gemini* for summarization.
- Efficiently summarizes videos, reducing viewing time while preserving essential information.

## Getting Started 🚀

### Prerequisites

- Python 3.10

### Usage

1. Clone the repository:
```
git clone https://github.com/viveknair6915/Video-Summarizer-System.git
```
2. create venv file and activate it
```
python -m venv .venv
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Create a ".env" file ⬇️
```
GOOGLE_GEMINI_API_KEY = "Your-Gemini-Key-Here"
```

### Get API Keys:

- [Google Gemini API key](https://makersuite.google.com/app/apikey) 🔑 
   

5 Run the summarizer:
```
streamlit run app.py
```
