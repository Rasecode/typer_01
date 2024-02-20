import os
import boto3


class TextRecognition:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    region = "us-east-1"
    service_name = "textract"

    def __init__(self):
        self.client = boto3.client(
            self.service_name,
            region_name=self.region,
            aws_access_key_id=self.WS_ACCESS_KEY_ID,
            aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
        )

    def ocr_recognition(self, image_bytes: bytes):
        assert isinstance(image_bytes, bytes)

        response = self.client.detect_document_text(Document={"Bytes": image_bytes})
        text = ""
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print(item["Text"])
                text = text + " " + item["Text"]

        return text
