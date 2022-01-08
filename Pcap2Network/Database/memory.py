from Pcap2Network.Database import Database


class RedisDatabase(Database):
    SCHEME = 'memory'

    def __init__(self, address):
        super().__init__(address)
        self._db = {}  # type: dict

    def connect(self):
        pass

    @property
    def is_connected(self):
        return True

    def __getitem__(self, item):
        return self._db[item]

    def __setitem__(self, key, value):
        self._db[key] = value

    def __repr__(self):
        return f'MemoryDatabase(keys={self._db.keys()})'
