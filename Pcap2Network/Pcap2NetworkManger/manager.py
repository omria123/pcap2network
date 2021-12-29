from ..Analyzer import Analyzer
from ..Database import Database
from ..WebServer import WebServer


class Pcap2NetworkManager:
    def __init__(self, db_address: str, web_server_port: int):
        self.db = Database(db_address)
        self.db.connect()
        self.web = WebServer(web_server_port)
        self.analyzer = Analyzer(self.db)

    def upload_pcap(self):
        pass

    def query_db(self):
        pass

    def plot(self):
        pass

    def start_webserver(self):
        self.web.run()
