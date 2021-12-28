import typing

from ..PcapParser import parse_pcap
from .layer2 import layer2_analyze_packet
from .layer3 import layer3_analyze_packet
from .layer4 import layer4_analyze_packet

if typing.TYPE_CHECKING:
    from typing import List

    from ..Database import Database
    from ..Lan import Lan
    from ..Machine import Machine


class Analyzer:
    ANALYZERS = [layer2_analyze_packet, layer3_analyze_packet, layer4_analyze_packet]

    def __init__(self, db):
        self.machines: List[Machine] = []
        self.networks: List[Lan] = []
        self.db: Database = db

    def load_pcap(self, pcap_path, pcap_metadata):
        packets = parse_pcap(pcap_path)
        for analyzer in self.ANALYZERS:
            for packet in packets:
                analyzer(self, packet, pcap_metadata)
        self.sync_db()

    def sync_db(self):
        pass
