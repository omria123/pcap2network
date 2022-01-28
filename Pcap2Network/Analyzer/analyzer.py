import typing
from pathlib import Path

from .sniffingcontext import SniffingContext
from .PacketAnalyzer import analyze_packet
from ..PcapParser import parse_pcap

if typing.TYPE_CHECKING:
    from typing import List, Union
    from ..PcapParser.metadata import PcapMetadata
    from ..Database import Database
    from ..Devices.Lan import Lan
    from ..Devices.Machine import Machine


class Analyzer:
    def __init__(self, db):
        self.machines = []  # type: List[Machine]
        self.networks = []  # type: List[Lan]
        self.db = db  # type: Database

    def load_pcap(self, pcap_path, pcap_metadata):
        # type: (Path, PcapMetadata) -> None
        packets = parse_pcap(pcap_path)
        sniffing_context = SniffingContext.from_metadata(pcap_metadata)
        for packet in packets:
            analyze_packet(self, packet, sniffing_context)

    def mac_to_machine(self, mac):
        # type: (str) -> Union[Machine, None]
        for machine in self.machines:
            if mac in [iface.mac for iface in machine.interfaces]:
                return machine

    def sync_db(self):
        pass

    def __repr__(self):
        st = 'Analyzer:'
        for network in self.networks:
            st += '\t' + repr(network).replace('\n', '\n\t')

        return st




