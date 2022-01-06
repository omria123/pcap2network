import typing

from .packet_analyzer import packet_analyzer

if typing.TYPE_CHECKING:
    from typing import Optional
    from .. import Analyzer
    from ..sniffingcontext import SniffingContext
    from ...PcapParser import Packet


def real_ipv4(address):
    # type: (str) -> bool
    """
    Returns whether the ipv4 address is real or some broadcast o placeholder
    :param address: Ipv4 address
    """
    if address in ['0.0.0.0', '255.255.255.255']:
        return False
    return True


def declare_ip_entity(analyzer, mac_addr, ipv4_addr, local=False, context=None):
    # type: (Analyzer, str, str, bool, Optional[SniffingContext]) -> None
    """
    Declare on new mac available in the Lan
    In case a sniffing context is given the mac will be added to the chosen context.
    :param analyzer: Analyzer which saves the machines.
    :param mac_addr: Mac from which the ipv4 came from.
    :param ipv4_addr: IP address.
    :param local: Whether the IP address is from the local lan.
    :param context: The sniffing context - where the packet is from.
    """
    # TODO: this
    pass


def arp_reply(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    declare_ip_entity(analyzer, packet['ARP']['hwsrc'], packet['ARP']['psrc'], local=True, context=context)
    declare_ip_entity(analyzer, packet['ARP']['hwdst'], packet['ARP']['pdst'], local=True, context=context)


def arp_request(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    declare_ip_entity(analyzer, packet['ARP']['hwsrc'], packet['ARP']['psrc'], local=True, context=context)


ARP_OPCODES = {1: arp_request, 2: arp_reply}


@packet_analyzer('ARP')
def arp_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    opcode = packet['ARP']['opcode']
    if opcode not in ARP_OPCODES:
        raise NotImplementedError(f'No support for ARP opcode - {opcode}')
    ARP_OPCODES[opcode](analyzer, packet, context)


@packet_analyzer('IP')
def ip_analyzer(analyzer, packet, context):
    # type: (Analyzer, Packet, SniffingContext) -> None
    dst = packet['IP']['dst']
    src = packet['IP']['src']
    src_mac = packet['Ether']['src']
    if real_ipv4(src):
        declare_ip_entity(analyzer, src, src_mac, context=context)
