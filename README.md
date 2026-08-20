# StreamHub — Video Streaming Platform

A full-stack video streaming platform built with **Python Flask, PostgreSQL, Bootstrap, FFmpeg, and AWS S3 integration**.

StreamHub allows users to create accounts, upload videos, automatically generate thumbnails, stream uploaded videos, manage their video library, and receive application notifications.

## Features

### Authentication

* User registration
* Secure password hashing
* User login and logout
* Session management using Flask-Login
* Protected routes
* User-specific access control

### Video Management

* Video upload
* Video format validation
* Secure and unique video filenames
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
* Watch controls
* Video deletion controls

### Notifications

* Automatic upload notifications
* Unread notification count
* Notification dropdown panel
* Individual notification deletion
* Clear-all notifications
* Notification timestamps

### Database

* PostgreSQL
* SQLAlchemy ORM
* Flask-Migrate / Alembic
* UUID-based identifiers
* Relationships between users, videos, and notifications

### User Interface

* Responsive Bootstrap interface
* Custom StreamHub branding
* Creator dashboard
* Search interface
* Notification panel
* Profile dropdown
* Responsive video cards

---

# Technology Stack

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
├── config.py
├── extensions.py
├── run.py
├── test_db.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

```

> Uploaded videos and generated thumbnails are intentionally excluded from GitHub through `.gitignore`. They are stored locally when the application is running.

---

# Requirements

Before running StreamHub, install:

* Python 3.14 or a compatible Python version
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

You should see `(venv)` in the command prompt.

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

Example:

```text
postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME

```

---

# Environment Configuration

Create a `.env` file in the project root.

Use `.env.example` as a template.

Example:

```env
SECRET_KEY=your-secret-key

DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME

FFMPEG_PATH=ffmpeg

```

### Important

Never commit the `.env` file to GitHub.

It may contain private credentials and configuration values.

The repository already includes `.gitignore` rules to prevent `.env` from being committed.

---

# FFmpeg Setup

StreamHub uses FFmpeg to generate thumbnails from uploaded videos.

Install FFmpeg on the machine running the application.

Verify the installation:

```bash
ffmpeg -version

```

If FFmpeg is available through the system PATH, use:

```env
FFMPEG_PATH=ffmpeg

```

If FFmpeg is installed in a custom location, provide the path to the executable:

```env
FFMPEG_PATH=C:\path\to\ffmpeg.exe

```

> The project does not depend on the developer's original local FFmpeg path. FFmpeg is configured through the `FFMPEG_PATH` environment variable.

---

# Database Migration

After configuring PostgreSQL and `.env`, run:

```bash
flask db upgrade

```

This creates or updates the required database tables using the project's Alembic migrations.

---

# Optional Database Connection Test

The repository includes `test_db.py` to verify PostgreSQL connectivity.

Run:

```bash
python test_db.py

```

A successful connection should display:

```text
Database connection successful!

```

---

# Run the Application

Start StreamHub:

```bash
python run.py

```

The Flask development server will start.

Open the application in your browser:

```text
http://127.0.0.1:5000

```

---

# Basic Usage

## 1. Create an Account

Open StreamHub and select:

```text
Create Account

```

Register a new user account.

## 2. Login

Log in using the registered credentials.

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

After uploading, StreamHub:

1. Stores the uploaded video locally.
2. Generates a unique filename.
3. Uses FFmpeg to generate a thumbnail.
4. Stores video metadata in PostgreSQL.
5. Creates an application notification.

## 4. Manage Videos

The creator dashboard displays uploaded videos.

Users can:

* Watch videos
* View video information
* Delete videos

## 5. Notifications

The notification bell displays application notifications.

Users can:

* View notifications
* Delete individual notifications
* Clear all notifications

---

# Database Models

The application uses database models for core entities including:

* Users
* Videos
* Notifications

The project uses UUID-based identifiers and relationships between the application's database entities.

---

# Security

The application includes:

* Password hashing using Werkzeug
* Authentication using Flask-Login
* Protected routes
* User-specific notification access
* User-specific video deletion authorization
* Secure uploaded filenames
* Video file extension validation
* Environment-based secrets
* Database credentials stored outside the source code

---

# File Storage

Uploaded videos and generated thumbnails are intentionally excluded from the Git repository.

The following directory is ignored:

```text
uploads/

```

This prevents large video files and user-generated media from being committed to GitHub.

For production deployment, the application's video storage can be moved to cloud object storage such as Amazon S3.

---

# Development Notes

StreamHub is currently designed to run locally using Flask's development server.

For production deployment, it is recommended to use:

* A production WSGI server
* Managed PostgreSQL
* Cloud object storage for videos
* HTTPS
* Production environment variables
* Secure cookie configuration
* Production logging
* Appropriate file-size and upload restrictions

---

# Troubleshooting

### PostgreSQL connection error

Check that:

1. PostgreSQL is running.
2. The database exists.
3. `DATABASE_URL` in `.env` is correct.
4. The PostgreSQL username and password are correct.

You can test the connection with:

```bash
python test_db.py

```

### FFmpeg not found

Run:

```bash
ffmpeg -version

```

If the command is not recognized, install FFmpeg and either add it to the system PATH or configure its executable location through:

```env
FFMPEG_PATH=C:\path\to\ffmpeg.exe

```

### Database tables missing

Run:

```bash
flask db upgrade

```

---

# Author

**Prathik Kumar P**

Computer Science & Engineering
Canara Engineering College

---

# Project Repository

[StreamHub Video Streaming Platform — GitHub](https://github.com/Prathikiee/streamhub-video-streaming-platform?utm_source=chatgpt.com)

# StreamHub - Video Streaming Platform

StreamHub is a Flask-based video streaming platform containerized with Docker
and deployed to Microsoft Azure using a fully automated CI/CD pipeline.

## Tech Stack

- Python
- Flask
- PostgreSQL / Supabase
- Docker
- GitHub
- Azure DevOps
- Azure Pipelines
- Azure Container Registry
- Azure App Service
- Gunicorn

## CI/CD Architecture

Developer
   ↓
GitHub Repository
   ↓
Azure Pipelines
   ↓
Docker Image Build
   ↓
Azure Container Registry
   ↓
Azure App Service
   ↓
Production Health Verification

## CI/CD Workflow

Whenever code is pushed to the `main` branch:

1. Azure Pipelines automatically detects the GitHub push.
2. The application Docker image is built.
3. The Docker image is pushed to Azure Container Registry.
4. The new image is deployed to Azure App Service.
5. The pipeline calls the production `/health` endpoint.
6. Deployment succeeds only when the application returns a healthy HTTP response.

## Pipeline Stages

### Build

Builds the StreamHub Docker image and pushes two tags:

- Build ID
- latest

### Deploy

Deploys the newly built Docker image from Azure Container Registry to
Azure App Service.

### Verify

After deployment, Azure Pipelines calls:

`/health`

Expected response:

```json
{
  "status": "healthy"
}
