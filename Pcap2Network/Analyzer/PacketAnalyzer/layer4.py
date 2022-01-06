import typing
from .packet_analyzer import packet_analyzer

if typing.TYPE_CHECKING:
    from ...Analyzer import Analyzer
    from ...Analyzer.sniffingcontext import SniffingContext
    from ...PcapParser import Packet


@packet_analyzer('TCP')
def tcp_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None

    dport = packet['TCP']['dport']
    sport = packet['TCP']['sport']
    return


@packet_analyzer('UDP')
def udp_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None

    dport = packet['UDP']['dport']
    sport = packet['UDP']['sport']
    return


@packet_analyzer('ICMP')
def icmp_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    return

