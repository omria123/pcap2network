from typing import Union
from urllib.parse import urlparse

from .database import Database

from redis import Redis, exceptions


class RedisHashMap:
    pass


class RedisDatabase(Database):
    SCHEME = 'redis'
    DEFAULT_PORT = 6379

    def __init__(self, address):
        super().__init__(address)
        up = urlparse(address)
        self.host = up.hostname  # type: str
        self.port = self.DEFAULT_PORT  # type: int
        if up.port is not None:
            self.port = up.port
        self._db = None  # type: Union[Redis, None]

    def connect(self):
        self._db = Redis(host=self.host, port=self.port)

    @property
    def is_connected(self):
        try:
            self._db.ping()
            return True
        except (exceptions.ConnectionError, ConnectionRefusedError):
            return False

    def __getitem__(self, item):
        return self.deserialize_value(self._db[item])

    def __setitem__(self, key, value):
        self._db[key] = self.serialize_value(value)

    def __repr__(self):
        return f'RedisDatabase({self.host}:{self.port})'

    @staticmethod
    def serialize_value(value):
        pass

    @staticmethod
    def deserialize_value(dump):
        pass
