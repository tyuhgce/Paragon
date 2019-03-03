import unittest

from core.image_service.dto.ImageDTO import ImageDTO
from core.image_service.image_processor import SimpleImageProcessor


class List(list):
    def __getitem__(self, index):
        if type(index) is int:
            return super(List, self).__getitem__(index)
        l = self
        for i in index:
            if not isinstance(l, list):
                raise IndexError('Too many indexes: out of depth.')
            l = l[i]
        return l


class SimpleImageProcessorTest(unittest.TestCase):
    def test_build_result_dto_dark(self):
        processor = SimpleImageProcessor()

        image_dto = ImageDTO(2, 2, List([[(1, 1, 1), (1, 1, 1)], [(1, 1, 1), (1, 1, 1)]]))
        r = processor.build_result_dto(image_dto)

        self.assertFalse(r.is_image_brightness)
        self.assertEqual(r.dark_pixels, 4)
        self.assertEqual(r.light_pixels, 0)

    def test_build_result_dto_light(self):
        processor = SimpleImageProcessor()

        image_dto = ImageDTO(2, 2, List([[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]]))
        r = processor.build_result_dto(image_dto)

        self.assertTrue(r.is_image_brightness)
        self.assertEqual(r.dark_pixels, 0)
        self.assertEqual(r.light_pixels, 4)

    def test_calc_pixel_brightness(self):
        processor = SimpleImageProcessor()
        c = processor.calc_pixel_brightness(0, 0, 0)
        self.assertEqual(c, 0)

        c = processor.calc_pixel_brightness(1, 1, 1)
        self.assertEqual(c, 0.2126 + 0.7152 + 0.1722)


if __name__ == '__main__':
    unittest.main()
