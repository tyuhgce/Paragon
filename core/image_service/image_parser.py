from abc import ABCMeta, abstractmethod
from PIL import Image

from core.image_service.dto.ImageDTO import ImageDTO


class ImageParser:
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_image_dto(self, data):
        """build image dto"""


class PILImageParser(ImageParser):
    def build_image_dto(self, data):
        im = Image.frombytes('RGB', (128, 128), data, 'raw')

        pix = im.load()
        width, height = im.size

        return ImageDTO(width, height, pix)
