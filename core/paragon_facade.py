from core.cahce_service.cache_service import FileCacheService
from core.image_service.image_parser import PILImageParser
from core.image_service.image_processor import SimpleImageProcessor


class ParagonCore:
    @staticmethod
    def get_image_parser():
        return PILImageParser()

    @staticmethod
    def get_image_processor():
        return SimpleImageProcessor()

    @staticmethod
    def get_cache_service():
        return FileCacheService()

    image_parser = get_image_parser.__func__()
    image_processor = get_image_processor.__func__()
    cache_service = get_cache_service.__func__()

    def prepare_image(self, data):
        pr = self.cache_service.get(data)
        if pr is not None:
            return pr.light_pixels, pr.dark_pixels, pr.is_image_brightness

        image_dto = self.image_parser.build_image_dto(data)
        pr = self.image_processor.build_result_dto(image_dto)

        self.cache_service.put(data, pr)

        return pr.light_pixels, pr.dark_pixels, pr.is_image_brightness
