from dotenv import load_dotenv
from file_1 import TextRecognition
from file_2 import TextCorrector
from mixins import ProcessImagesMixin


load_dotenv()


class ImageTextPipeline(ProcessImagesMixin):
    text_recognizer = TextRecognition()
    text_corrector = TextCorrector()

    def __init__(self, image_urls: list[str]):
        assert isinstance(image_urls, list)

        self.image_urls = image_urls

    def process(self):
        all_text = ""
        print("Inicia")

        image_bytes = self.process_images(self.image_urls)
        for image_byte in image_bytes:
            extracted_text = self.text_recognizer.ocr_recognition(image_byte)
            all_text += extracted_text + "\n"

        # Corrige el texto extraído
        corrected_text = self.text_corrector.generate_description(all_text)
        return corrected_text


if __name__ == "__main__":
    # Lista de URLs de imágenes
    image_urls = [
        "https://istolacio-production.s3.amazonaws.com/media/capture/27-10-2023-103852231283.png",
        "https://istolacio-production.s3.amazonaws.com/media/capture/27-10-2023-103951999380.png",
        # Agrega más URLs según sea necesario
    ]

    pipeline = ImageTextPipeline(image_urls)
    corrected_text = pipeline.process()
    print("Texto corregido:\n", corrected_text)
