PROTOCOLS = {}


def protocol_analyzer(protocol_name):
    def decorator(f):
        PROTOCOLS[protocol_name] = f
        return f

    return decorator


def analyze_metadata(db, metadata):
    pass


def layer4_analyze_packet(db, packet, pcap_metadata):
    analyze_metadata(db, pcap_metadata)
    for protocol in PROTOCOLS:
        if protocol in packet:
            PROTOCOLS[protocol](db, packet, pcap_metadata)

    return


@protocol_analyzer('TCP')
def ether_analyzer(db, packet, pcap_metadata):
    dport = packet['TCP'].dport
    sport = packet['TCP'].sport
    return


@protocol_analyzer('UDP')
def ether_analyzer(db, packet, pcap_metadata):
    dport = packet['UDP'].dport
    sport = packet['UDP'].sport
    return


@protocol_analyzer('ICMP')
def ether_analyzer(db, packet, pcap_metadata):
    return
