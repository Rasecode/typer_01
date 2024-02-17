import boto3
import io
from PIL import Image
import requests
from file_1 import text_recognition
from file_2 import text_corrector

class ImageTextPipeline:
    def __init__(self):
        self.text_recognizer = text_recognition()
        self.text_corrector = text_corrector()

    def process_images(self, image_urls):
        all_text = ""
        print("Inicia")
        for url in image_urls:
            # Descarga la imagen
            response = requests.get(url)
            image_bytes = response.content
            # Extrae el texto de la imagen
            extracted_text = self.text_recognizer.ocr_recognition(image_bytes)
            all_text += extracted_text + "\n"

        # Corrige el texto extraído
        corrected_text = self.text_corrector.generate_description(all_text)
        return corrected_text

if __name__ == "__main__":
    # Lista de URLs de imágenes
    image_urls = [
        "https://istolacio-production.s3.amazonaws.com/media/capture/27-10-2023-103852231283.png",
        "https://istolacio-production.s3.amazonaws.com/media/capture/27-10-2023-103951999380.png"
        # Agrega más URLs según sea necesario
    ]

    pipeline = ImageTextPipeline()
    corrected_text = pipeline.process_images(image_urls)
    print("Texto corregido:\n", corrected_text)
