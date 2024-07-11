import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

cloudinary.config(
  cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
  api_key = os.getenv("CLOUDINARY_API_KEY"),
  api_secret = os.getenv("CLOUDINARY_API_SECRET")
)

def upload_avatar(file_path):
    result = cloudinary.uploader.upload(file_path)
    return result['url']
