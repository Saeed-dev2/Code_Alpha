# Cloud-Based Photo Gallery

## Project Overview
The **Cloud-Based Photo Gallery** is a web application that allows users to upload and view images stored securely in an AWS S3 bucket. The backend is built using Flask, a Python web framework, while the frontend uses HTML and JavaScript for user interaction. The application supports image uploads, dynamic gallery updates, and seamless integration between the backend and cloud storage.

---

## Features
- **Image Upload**: Users can upload images directly to an AWS S3 bucket via the web interface.
- **Image Gallery**: Displays all images stored in the S3 bucket in a user-friendly gallery format.
- **CORS Support**: Enables smooth interaction between the frontend and the Flask backend.

---

## Prerequisites
Before starting, ensure you have the following:
- **Python 3.x**: The backend is implemented in Python.
- **Flask**: Install using `pip install flask`.
- **Flask-CORS**: Install using `pip install flask-cors`.
- **Boto3**: Install using `pip install boto3`.
- **AWS Account**: Create an S3 bucket in your AWS account.
- **AWS Access Key and Secret Key**: Generate these from the AWS IAM console.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/cloud-based-photo-gallery.git
cd cloud-based-photo-gallery
```

## Install Dependencies
```bash
pip install -r requirements.txt
```
## python app.py

```bash
python app.py
```
