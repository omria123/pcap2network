import typing

from ..Lan import Lan
from ..Machine import Interface
from ..Machine import Machine

if typing.TYPE_CHECKING:
    from .analyzer import Analyzer

PROTOCOLS = {}
GLOBAL_MACS = ['FF:FF:FF:FF:FF:FF']


def protocol_analyzer(protocol_name):
    def decorator(f):
        PROTOCOLS[protocol_name] = f
        return f

    return decorator


def analyze_metadata(analyzer: Analyzer, metadata):
    context = {'network': Lan()}
    if 'network' in metadata:
        context['network'] = metadata['network']
    if 'interface' in metadata:
        metadata['interface']  # TODO feed interface to analyzer
    return context


def layer2_analyze_packet(analyzer: Analyzer, packet, pcap_metadata):
    context = analyze_metadata(analyzer, pcap_metadata)
    for protocol in PROTOCOLS:
        if protocol in packet:
            PROTOCOLS[protocol](analyzer, packet, context)


def declare_layer2_entity(analyzer: Analyzer, mac_addr: str, network: Lan = None):
    for machine in analyzer.machines:
        for interface in machine.interfaces:
            if interface.mac == mac_addr:
                # Already declared
                return
    analyzer.machines.append(Machine(interfaces=[Interface(mac_addr, network=network)]))


@protocol_analyzer('Ether')
def ether_analyzer(analyzer: Analyzer, packet, context):
    dst = packet['Ether'].dst
    src = packet['Ether'].src
    declare_layer2_entity(analyzer, src, context['network'])
    if dst not in GLOBAL_MACS:
        declare_layer2_entity(analyzer, src, context['network'])
