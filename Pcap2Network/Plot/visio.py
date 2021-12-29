import typing
from pathlib import Path

if typing.TYPE_CHECKING:
    from ..Database import Database


class VisioPlotter:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def plot(self, filename: str, db: Database):
        path = self.output_dir / filename

