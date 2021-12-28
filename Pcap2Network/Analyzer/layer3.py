PROTOCOLS = {}


def protocol_analyzer(protocol_name):
    def decorator(f):
        PROTOCOLS[protocol_name] = f
        return f

    return decorator


def analyze_metadata(db, metadata):
    pass


def layer3_analyze_packet(db, packet, pcap_metadata):
    analyze_metadata(db, pcap_metadata)
    for protocol in PROTOCOLS:
        if protocol in packet:
            PROTOCOLS[protocol](db, packet, pcap_metadata)

    return


@protocol_analyzer('ARP')
def ether_analyzer(db, packet, pcap_metadata):
    return


@protocol_analyzer('DHCP')
def ether_analyzer(db, packet, pcap_metadata):
    return


@protocol_analyzer('IP')
def ether_analyzer(db, packet, pcap_metadata):
    dst = packet['IP'].dst
    src = packet['IP'].src
    return
