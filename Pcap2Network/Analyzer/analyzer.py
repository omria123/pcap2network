from ..PcapParser import parse_pcap
from .layer2 import layer2_analyze_packet
from .layer3 import layer3_analyze_packet
from .layer4 import layer4_analyze_packet


class Analyzer:
    ANALYZERS = [layer2_analyze_packet, layer3_analyze_packet, layer4_analyze_packet]

    def __init__(self, db):
        self.db = db

    def load_pcap(self, pcap_path, pcap_metadata):
        packets = parse_pcap(pcap_path)
        for analyzer in self.ANALYZERS:
            for packet in packets:
                analyzer(self.db, packet, pcap_metadata)
