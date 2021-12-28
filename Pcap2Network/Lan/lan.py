class Lan:
    def __init__(self, interfaces=None):
        self.interfaces = interfaces
        if interfaces is None:
            self.interfaces = None
        self._sync_interfaces()

    def _sync_interfaces(self):
        for i in self.interfaces:
            i.network = self

    def add_interface(self, interface):
        self.interfaces.append(interface)
        interface.network = self
