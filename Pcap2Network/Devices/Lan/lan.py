import typing

if typing.TYPE_CHECKING:
    from typing import List

    from ..Machine import Interface


class Lan:
    def __init__(self, interfaces=None):
        self.interfaces: List[Interface] = interfaces
        if interfaces is None:
            self.interfaces = None
        self._sync_interfaces()

    def _sync_interfaces(self):
        for i in self.interfaces:
            i.network = self

    def add_interface(self, interface):
        self.interfaces.append(interface)
        interface.network = self

    @classmethod
    def merge_networks(cls, lan1, lan2):
        if lan1 is lan2:
            return
        # TODO: According to Mac
        return cls(list(set(lan1.interfaces + lan2.interfaces)))

    def __repr__(self):
        st = 'Network:'
        for interface in self.interfaces:
            st += '\t' + repr(interface.machine).replace('\n', '\n\t')

        return st
