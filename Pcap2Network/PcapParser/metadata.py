class PcapMetadata:
    def __init__(self, mac, interface_name=None):
        self.mac = mac  # type: str
        self.interface_name = interface_name  # type: str

    def dumps(self):
        pass

    @classmethod
    def loads(cls):
        pass
