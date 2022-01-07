from .database import Database


class RedisDatabase(Database):
    SCHEME = 'redis'

    def __init__(self, address):
        super().__init__(address)

    def connect(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def disconnect(self):
        pass

    def __repr__(self):
        return f'RedisDatabase({self.address})'
