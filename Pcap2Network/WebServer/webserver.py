import typing

if typing.TYPE_CHECKING:
    from ..Database import Database
    from typing import Union


class WebServer:
    DEFAULT_PORT = 8080

    def __init__(self, port=DEFAULT_PORT, db=None):
        # type: (int, Database) -> None
        self.port = port  # type: int
        self.db = db  # type: Union[Database, None]

    def upload_pcap(self):
        """
        Gets a POST request and receive the pcap to analyze it.
        """

    def run_query(self):
        """
        Run query to the DB and return the results.
        """

    def run(self):
        """
        Start the server with all of it's functions
        """
