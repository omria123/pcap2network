from typing import List, Dict

from ..Lan import Lan


class Interface:
    def __init__(self, mac, machine=None, network=None, ipv4=None, name=None):
        self.mac = mac
        self.ipv4 = ipv4
        self.machine = machine
        self.network = network
        self.name = name

        if network is None:
            self.network = Lan(interfaces=[self])

    def __repr__(self):
        st = f'{self.name}: MAC={self.mac}'
        if self.ipv4 is None:
            return st
        if isinstance(self.ipv4, str):
            st += f', IPv4={self.ipv4}'
        else:
            raise NotImplementedError('No support for more representation')
        return st

    @classmethod
    def merge_interfaces(cls, interface1, interface2):
        # type: (Interface, Interface) -> Interface
        if interface1.mac != interface2.mac:
            raise ValueError('Can\'t merge interfaces with different macs')


class InterfaceCollection:
    def __init__(self, *interfaces):
        # type: (*Interface) -> None
        self.interfaces = {i.mac: i for i in interfaces}  # type: Dict[str, Interface]

    def __getitem__(self, item):
        # type: (str) -> Interface
        if item in self.interfaces:
            return self.interfaces[item]

        raise KeyError(f'Interface with {item} wasn\'t found')

    def __iter__(self):
        return self.interfaces.__iter__()

    def __contains__(self, item):
        return item in self.interfaces

    def add_interface(self, iface):
        if iface.mac not in self.interfaces:
            self.interfaces[iface.mac] = iface
        # TODO: ELSE
