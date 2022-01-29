from Pcap2Network.PcapParser import PcapMetadata

import pytest


@pytest.mark.parametrize('pcap,expected_macs', [
    ('simple_lan.pcapng', ["18:47:3d:42:a1:2f",
                           "01:00:5e:00:00:fb",
                           "01:00:5e:11:91:91",
                           "01:00:5e:72:72:72",
                           "01:00:5e:7f:ff:fa",
                           "33:33:00:00:00:fb",
                           "4c:17:eb:ea:6f:ca",
                           "ec:fa:bc:bc:c6:0e",
                           ])
])
def test_entities_scan(analyzer, shared_datadir, pcap, expected_macs):
    pcap_path = shared_datadir / pcap
    assert pcap_path.exists()

    analyzer.load_pcap(pcap_path, pcap_metadata=PcapMetadata(expected_macs[0], 'eth0'))
    lan = analyzer.networks[0]
    assert set(i.mac for i in lan.interfaces) == set(expected_macs)
