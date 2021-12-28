class Machine(object):
    _ID = 0
    ALL = []

    def __init__(self, os=None, interfaces=None):
        self.os = os
        self.interfaces = []
        if interfaces is not None:
            self.interfaces = interfaces
        self.id = self._ID
        self._ID += 1
        self._sync_interfaces()

    def __repr__(self):
        st = f'Machine {self.os}\n'
        st += 'Interfaces:\n'
        st += '\n'.join(repr(i for i in self.interfaces))
        return st

    def add_interface(self, interface):
        self.interfaces.append(interface)
        interface.machine = self

    def _sync_interfaces(self):
        for i in self.interfaces:
            i.machine = self
