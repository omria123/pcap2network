from typing import List
from pathlib import Path

PARSERS = {}


def parser(name):
    def decorator(f):
        PARSERS[name] = f
        return f

    return decorator


@parser('scapy')
def scapy_parse_pcap(path: Path):
    from scapy.all import rdpcap
    return rdpcap(str(path))


def parse_pcap(path: Path, pcap_parser: str = 'scapy') -> List:
    """
    Reads pcap to
    :param path: path to pcap
    :param pcap_parser: select a parser for the pcap file
    :return: List of packets
    """
    return PARSERS[pcap_parser](path)
