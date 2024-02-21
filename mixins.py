import requests
from requests.exceptions import RequestException


class ProcessImagesMixin:
    def process_images(self, image_urls: list[str]):
        assert isinstance(image_urls, list)

        image_bytes = []
        for url in self.image_urls:
            image_byte = self._process_image(url)
            if image_byte is None:
                continue

            image_bytes.append(image_byte)
        return image_bytes

    def _process_image(self, url: str):
        assert isinstance(url, str)

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return None
            return response.content
        except RequestException:
            return None
