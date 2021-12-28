class Machine(object):
    ALL = []

    def __init__(self, os=None, interfaces=None):
        self.os = os
        self.interfaces = []
        if interfaces is not None:
            self.interfaces = interfaces
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

    @classmethod
    def merge_machines(cls, machine1, machine2):
        interfaces = machine1.interfaces
        macs = [i.mac for i in interfaces]
        for interface in machine2.interfaces:
            if interface.mac in macs:




        cls(machine1.os or machine2.os)
        if machine1.os is not None and machine2.os is not None and machine1.os != machine2.os:
            pass
            # TODO: Add logging alert that a conflict just happened. Printing an identifier and the relevant OSes.

