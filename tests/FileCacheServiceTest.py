import unittest

from core.cahce_service.cache_service import FileCacheService


class FileCacheServiceTest(unittest.TestCase):
    def test_is_present(self):
        cache_service = FileCacheService()
        self.assertFalse(cache_service.is_present("obj"))

        cache_service.put("obj", "pr")
        self.assertTrue(cache_service.get("obj"))

    def test_get_put(self):
        cache_service = FileCacheService()

        pr = "pr"
        obj = "obj"
        cache_service.put(obj, pr)
        self.assertTrue(cache_service.is_present(obj))
        self.assertEqual(pr, cache_service.get(obj))


if __name__ == '__main__':
    unittest.main()
