from Pcap2Network.Analyzer import Analyzer
from Pcap2Network.Database import Database

import pytest


@pytest.fixture
def db():
    return Database('memory://')


@pytest.fixture
def analyzer(db):
    return Analyzer(db)
