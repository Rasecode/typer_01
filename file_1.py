import boto3
import os
import io
from PIL import Image, ImageDraw
from dotenv import load_dotenv


class text_recognition:
    def __init__(self):
        load_dotenv()
        AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.client = boto3.client('textract',region_name='us-east-1',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def ocr_recognition(self, image_bytes):

        # buffer = io.BytesIO()
        # image_jpg.save(buffer, format='JPEG')
        # buffer.seek(0)

        # img = bytearray(buffer.read())

        response = self.client.detect_document_text(
            Document={'Bytes': image_bytes}
        )
        text = ""
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print (item["Text"])
                text = text + " "+item["Text"]

        return text