from abc import ABCMeta, abstractmethod
from core.image_service.dto.ProcessorResult import ProcessorResult
from core.image_service.image_parser import PILImageParser


class ImageProcessor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_result_dto(self, image_dto):
        """build result dto"""

    @abstractmethod
    def calc_pixel_brightness(self, red, green, blue):
        """calc pixel brightness"""


class SimpleImageProcessor(ImageProcessor):
    def calc_pixel_brightness(self, red, green, blue):
        return 0.2126 * red + 0.7152 * green + 0.1722 * blue

    @property
    def get_image_parser(self):
        return PILImageParser()

    def build_result_dto(self, image_dto):
        middle_brightness = 127.5
        light_pixel_counter = 0
        dark_pixel_counter = 0
        for i in range(image_dto.width):
            for j in range(image_dto.height):
                red, green, blue = image_dto.pixels[i, j]
                pixel_brightness = self.calc_pixel_brightness(red, green, blue)

                if pixel_brightness > middle_brightness:
                    light_pixel_counter += 1
                else:
                    dark_pixel_counter += 1

        return ProcessorResult(light_pixel_counter, dark_pixel_counter)
