class Machine(object):
    ALL = []

    def __init__(self, os=None, interfaces=None):
        self.os = os
        self.interfaces = []
        if interfaces is not None:
            self.interfaces = interfaces
        self._sync_interfaces()

    def __repr__(self):
        st = f'Machine:'

        if self.os is None:
            st += f' {self.os}'
        st += '\n'
        for interface in self.interfaces:
            st += '\t' + repr(interface).replace('\n', '\n\t')
        return st

    def add_interface(self, interface):
        self.interfaces.append(interface)
        interface.machine = self

    def _sync_interfaces(self):
        for i in self.interfaces:
            i.machine = self

    @classmethod
    def merge_machines(cls, machine1, machine2):
        interfaces = machine1.interfaces
        macs = {i.mac: i for i in interfaces}
        for interface in machine2.interfaces:
            if interface.mac in macs:
                other_interface = macs[interface.mac]
                interfaces.remove(other_interface)
                interfaces.append(interface.merge_interfaces(interface, macs[interface.mac]))

        if machine1.os is not None and machine2.os is not None and machine1.os != machine2.os:
            pass
            # TODO: Add logging alert that a conflict just happened. Printing an identifier and the relevant OSes.

        return cls(machine1.os or machine2.os, interfaces)

#### Merges Diagram #####
# m1, m2 Merge -> m1.interfaces, m2.interfaces merge -> (if same interface) i1.network, i2.network merge -> all interfaces in both lans should be in a new lan
