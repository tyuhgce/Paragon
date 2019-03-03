from abc import ABCMeta, abstractmethod


class AbstractCacheWService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_present(self, obj):
        """Is there a object in cache"""

    @abstractmethod
    def put(self, obj, pr):
        """put a object to cache"""

    @abstractmethod
    def get(self, obj):
        """get a object from cache"""


class FileCacheService(AbstractCacheWService):
    map = {}

    def is_present(self, obj):
        return obj in self.map

    def put(self, obj, pr):
        self.map[obj] = pr

    def get(self, obj):
        return self.map.get(obj)


assert issubclass(FileCacheService, AbstractCacheWService)
