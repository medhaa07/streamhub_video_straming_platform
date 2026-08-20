# StreamHub — Video Streaming Platform

A full-stack video streaming platform built with **Python Flask, PostgreSQL, Bootstrap, FFmpeg, and AWS S3 integration**.

StreamHub allows users to create accounts, upload videos, automatically generate thumbnails, stream uploaded videos, manage their video library, and receive real-time application notifications.

## Features

### Authentication

* User registration
* Secure password hashing
* User login and logout
* Session management using Flask-Login
* Protected routes

### Video Management

* Upload videos
* Video format validation
* Automatic unique video filenames
* Automatic thumbnail generation using FFmpeg
* Video streaming
* Video view tracking
* Video deletion
* Video categories
* Public/private visibility
* Video descriptions

### Creator Dashboard

* Total video count
* Total views
* Storage information
* Personal video library
* Video preview thumbnails
* Watch and delete controls

### Notifications

* Automatic upload notifications
* Notification badge with unread count
* Custom notification panel
* Individual notification deletion
* Clear-all notifications
* Notification timestamps

### Database

* PostgreSQL
* SQLAlchemy ORM
* Flask-Migrate / Alembic
* UUID-based primary keys
* Database relationships between users, videos, and notifications

### UI

* Responsive Bootstrap interface
* Custom StreamHub branding
* Creator dashboard
* Search interface
* Notification panel
* Profile dropdown
* Responsive video cards

---

## Technology Stack

| Technology              | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| Python                  | Backend programming                       |
| Flask                   | Web framework                             |
| Flask-SQLAlchemy        | Database ORM                              |
| PostgreSQL              | Database                                  |
| Flask-Migrate           | Database migrations                       |
| Flask-Login             | Authentication                            |
| Flask-WTF               | Forms and validation                      |
| Werkzeug                | Password hashing and security             |
| FFmpeg                  | Video processing and thumbnail generation |
| Bootstrap               | Frontend UI                               |
| Jinja2                  | Server-side templates                     |
| AWS S3 / Boto3          | Cloud storage integration                 |
| HTML / CSS / JavaScript | Frontend                                  |

---

# Project Structure

```text
streamhub-video-streaming-platform/
│
├── app/
│   ├── blueprints/
│   ├── dashboard/
│   ├── home/
│   ├── auth/
│   ├── notification/
│   ├── video/
│   ├── stream/
│   └── models/
│
├── migrations/
│   └── versions/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── uploads/
│   ├── videos/
│   └── thumbnails/
│
├── config.py
├── extensions.py
├── run.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> The `uploads/` directory is ignored by Git. Uploaded videos and generated thumbnails are stored locally when the application is running.

---

# Requirements

Before running StreamHub, install:

* Python 3.14 or compatible Python version
* PostgreSQL
* FFmpeg
* Git

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Prathikiee/streamhub-video-streaming-platform.git
```

Enter the project directory:

```bash
cd streamhub-video-streaming-platform
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see:

```text
(venv)
```

before your command prompt.

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Configuration

StreamHub uses PostgreSQL as its database.

Create a PostgreSQL database and obtain its connection details.

The application expects a `DATABASE_URL` environment variable.

For example:

```text
postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME
```

---

# Environment Configuration

Create a `.env` file in the project root.

You can use `.env.example` as a template.

Copy:

```text
.env.example
```

to:

```text
.env
```

Then configure:

```env
SECRET_KEY=your-secret-key

DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME

FFMPEG_PATH=ffmpeg
```

### Important

Never commit `.env` to GitHub.

The `.env` file contains private configuration such as database credentials.

---

# FFmpeg Setup

StreamHub uses FFmpeg to generate video thumbnails.

Download and install FFmpeg on the machine running the application.

After installation, verify it:

```bash
ffmpeg -version
```

If FFmpeg is available through the system PATH, use:

```env
FFMPEG_PATH=ffmpeg
```

If FFmpeg is installed in a custom location, specify the full executable path:

```env
FFMPEG_PATH=C:\path\to\ffmpeg.exe
```

---

# Database Migration

After configuring PostgreSQL and `.env`, run:

```bash
flask db upgrade
```

This creates/updates the required database tables.

---

# Run the Application

Start StreamHub with:

```bash
python run.py
```

The Flask development server will start.

Open the application in your browser at:

```text
http://127.0.0.1:5000
```

---

# Basic Usage

## 1. Create an Account

Open the application and select:

```text
Create Account
```

Register a new user.

## 2. Login

Log in using your registered credentials.

## 3. Upload a Video

Open the creator dashboard and select:

```text
Upload Video
```

Provide:

* Video file
* Title
* Description
* Category
* Visibility

After upload, StreamHub:

1. Stores the video.
2. Generates a unique filename.
3. Uses FFmpeg to generate a thumbnail.
4. Stores the video information in PostgreSQL.
5. Creates a notification for the user.

## 4. Manage Videos

The dashboard displays the creator's uploaded videos.

Users can:

* Watch videos
* View video information
* Delete videos

## 5. Notifications

The notification bell displays recent notifications.

Users can:

* View notifications
* Delete individual notifications
* Clear all notifications

---

# Database Models

The application currently uses database models for core entities including:

* Users
* Videos
* Notifications

User IDs and related foreign keys use PostgreSQL UUID types.

---

# Security

The application includes:

* Password hashing using Werkzeug
* Authentication using Flask-Login
* Protected routes
* User-specific notification access
* User-specific video deletion authorization
* Secure uploaded filenames
* File extension validation
* Environment-based secrets
* Database credentials stored outside the source code

---

# GitHub and Uploaded Media

Uploaded videos are intentionally excluded from the Git repository.

The following directory is ignored:

```text
uploads/
```

This prevents large video files and user-generated media from being committed to GitHub.

For production deployment, video storage can be moved to cloud storage such as Amazon S3.

---

# Development Notes

This project is currently designed to run locally using the Flask development server.

For production deployment, it is recommended to use:

* A production WSGI server
* Managed PostgreSQL
* Cloud object storage for videos
* HTTPS
* Production environment variables
* Proper production logging
* Secure cookie configuration

---

# Author

**Prathik Kumar P**

Computer Science & Engineering

Canara Engineering College

---

# Project Repository

GitHub:

https://github.com/Prathikiee/streamhub-video-streaming-platform
