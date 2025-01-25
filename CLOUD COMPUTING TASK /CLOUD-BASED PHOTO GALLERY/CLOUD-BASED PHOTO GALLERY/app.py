import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend to interact with backend

# AWS S3 Configuration
AWS_S3_BUCKET = 'your-s3-bucket-name'
AWS_ACCESS_KEY = 'your-aws-access-key'
AWS_SECRET_KEY = 'your-aws-secret-key'
S3_REGION = 'us-east-1'

# Allowed extensions for photos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the S3 client
s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                         aws_secret_access_key=AWS_SECRET_KEY, region_name=S3_REGION)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        try:
            # Upload file to S3
            s3_client.upload_fileobj(file, AWS_S3_BUCKET, filename)
            file_url = f'https://{AWS_S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}'
            return jsonify({'message': 'File uploaded successfully', 'file_url': file_url}), 200
        except Exception as e:
            return jsonify({'message': f'Error uploading file: {str(e)}'}), 500

@app.route('/list', methods=['GET'])
def list_files():
    try:
        # List files in the S3 bucket
        response = s3_client.list_objects_v2(Bucket=AWS_S3_BUCKET)
        files = []
        if 'Contents' in response:
            for obj in response['Contents']:
                files.append(obj['Key'])
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'message': f'Error retrieving files: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
