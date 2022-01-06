import typing

from .packet_analyzer import packet_analyzer
from ...Devices.Lan import Lan
from ...Devices.Machine import Interface
from ...Devices.Machine import Machine

if typing.TYPE_CHECKING:
    from typing import Optional
    from ...Analyzer.sniffingcontext import SniffingContext
    from ...PcapParser import Packet
    from ...Analyzer.analyzer import Analyzer


def is_unicast(mac):
    # type: (str) -> bool
    return int(mac.split(':')[0], 16) & 1 == 0


def declare_layer2_entity(analyzer, mac_addr, context=None):
    # type: (Analyzer, str, Optional[SniffingContext]) -> None
    """
    Declare on new mac available in the Lan
    In case a sniffing context is given the mac will be added to the chosen context.
    :param analyzer: Analyzer which saves the machines.
    :param mac_addr: Address to declare on.
    :param context: The sniffing context - where the packet is from.
    """

    if analyzer.mac_to_machine(mac_addr) is not None:
        return

    network = Lan() if context is None else context.lan
    analyzer.machines.append(Machine(interfaces=[Interface(mac_addr, network=network)]))


@packet_analyzer('Ether')
def ether_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    """
    Analyze the Ether layer in the packet.
    Declare every new entity in the lan.
    :param analyzer: Analyzer which saves the machines
    :param packet: The packet to analyze
    :param context: The sniffing context - where the packet is from
    """
    dst = packet['Ether']['dst']
    src = packet['Ether']['src']
    declare_layer2_entity(analyzer, src, context)
    if is_unicast(dst):
        declare_layer2_entity(analyzer, dst, context)
