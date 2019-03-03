from abc import ABCMeta, abstractmethod
from PIL import Image
import io

from core.image_service.dto.ImageDTO import ImageDTO


class ImageParser:
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_image_dto(self, data):
        """build image dto"""


class PILImageParser(ImageParser):
    def build_image_dto(self, data):
        image_stream = io.BytesIO(data.data)
        im = Image.open(image_stream)

        pix = im.load()
        width, height = im.size

        return ImageDTO(width, height, pix)
