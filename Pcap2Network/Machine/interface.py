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
        if interface1.mac != interface2.mac:
            raise ValueError('Can\'t merge interfaces with different macs')
        return cls(interface1.mac,)