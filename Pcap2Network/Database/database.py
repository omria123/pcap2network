from typing import Any


class Database:
    SCHEME = None

    def __new__(cls, url, *args, **kwargs):
        # type: (Database, str, *Any, **Any) -> Database
        subclass_map = {subclass.SCHEME: subclass for subclass in cls.__subclasses__()}
        scheme, _ = url.split('://', 1)
        if scheme not in subclass_map:
            raise NotImplementedError(f'No support for scheme: {scheme}://')
        subclass = subclass_map[scheme]
        return super(Database, subclass).__new__(subclass)

    def __init__(self, url):
        _, self.address = url.split('://', 1)

    def connect(self):
        raise NotImplementedError('Abstract method')

    def __getitem__(self, item):
        raise NotImplementedError('Abstract method')

    def __setitem__(self, key, value):
        raise NotImplementedError('Abstract method')
