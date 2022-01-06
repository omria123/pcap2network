from typing import List, Dict, Union, Iterable
from pathlib import Path

PARSERS = {}

Packet = Dict[str, Dict[str, Union[str, int]]]


def parser(name):
    def decorator(f):
        PARSERS[name] = f
        return f

    return decorator


@parser('scapy')
def scapy_parse_pcap(path):
    # type: (Path) -> Iterable[Packet]
    from scapy.all import rdpcap
    return rdpcap(str(path))


def parse_pcap(path, pcap_parser='scapy'):
    # type: (Path, str) -> Iterable[Packet]
    """
    Reads pcap to
    :param path: path to pcap
    :param pcap_parser: select a parser for the pcap file
    :return: List of packets
    """
    return PARSERS[pcap_parser](path)
