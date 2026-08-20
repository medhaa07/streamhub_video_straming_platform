# StreamHub

A modern video streaming platform built using Flask and PostgreSQL.

## Features

- User Authentication
- Video Upload
- Video Streaming
- Thumbnail Generation (FFmpeg)
- Creator Dashboard
- Notification System
- Delete Videos
- Responsive Glassmorphism UI
- PostgreSQL Database
- Bootstrap 5 Interface

## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Login
- Flask-Migrate
- Bootstrap 5
- FFmpeg
- HTML
- CSS
- JavaScript

## Installation

```bash
git clone https://github.com/yourusername/streamhub-video-streaming-platform.git

cd streamhub-video-streaming-platform

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

flask db upgrade

python run.py
