from ..Analyzer import Analyzer
from ..Database import Database


class Pcap2NetworkManager:
    def __init__(self, db_address):
        self.db = Database(db_address)
        self.db.connect()
        self.analyzer = Analyzer(self.db)

    def upload_pcap(self):
        pass

    def query_db(self):
        pass

    def plot(self):
        pass
