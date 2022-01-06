import typing

from ..Devices.Lan import Lan
from ..Devices.Machine import Interface
from ..Devices.Machine import Machine

if typing.TYPE_CHECKING:
    from typing import Optional
    from ..PcapParser import PcapMetadata


class SniffingContext:
    def __init__(self, interface: Interface):
        self.interface = interface  # type: Interface

    @property
    def lan(self):
        # type: () -> Lan
        return self.interface.network

    @property
    def machine(self):
        # type: () -> Machine
        return self.interface.machine

    @property
    def ipv4(self):
        # type: () -> str
        return self.interface.ipv4

    @classmethod
    def from_metadata(cls, metadata):
        # type: (PcapMetadata) -> SniffingContext
        # TODO: bind ipv4 from metadata if exists
        m = Machine(interfaces=[Interface(metadata.mac, network=Lan())])
        return cls(m.interfaces[0])
