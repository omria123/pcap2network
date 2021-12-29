import argparse

from Pcap2Network.Pcap2NetworkManger import Pcap2NetworkManager


def get_args():
    parser = argparse.ArgumentParser(description='Start analyzer')
    parser.add_argument('--db-address', type=str, help='url to database like mongo://<IP>:<Port>')
    parser.add_argument('-p', '--web-port', type=int, help='Port to listen on for the webserver')

    return parser.parse_args()


def main(args):
    manager = Pcap2NetworkManager(args.db_address, args.web_port)
    manager.start_webserver()


if __name__ == '__main__':
    main(get_args())
