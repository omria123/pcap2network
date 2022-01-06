import typing

if typing.TYPE_CHECKING:
    from Pcap2Network.Analyzer.analyzer import Analyzer
    from Pcap2Network.PcapParser import Packet
    from Pcap2Network.Analyzer.sniffingcontext import SniffingContext

PROTOCOLS = {}


def packet_analyzer(protocol_name):
    # type: ignore
    def decorator(f):
        PROTOCOLS[protocol_name] = f
        return f

    return decorator


def analyze_packet(analyzer, packet, sniffing_context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    for protocol in PROTOCOLS:
        if protocol in packet:
            PROTOCOLS[protocol](analyzer, packet, sniffing_context)
