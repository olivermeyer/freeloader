from dataclasses import dataclass
from typing import Annotated
from urllib.parse import quote

from prettytable import PrettyTable

TimeInMs = Annotated[int, "Duration in milliseconds"]


@dataclass(frozen=True)
class TrackInfo:
    artist: str
    title: str

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"


@dataclass
class Tracklist(dict):
    def print(self, include_search_links: bool):
        """Print the tracklist to stdout."""

        def format_timestamp(ms: TimeInMs) -> str:
            return f"{ms // 3600000}:{(ms // 60000) % 60:02d}:{(ms // 1000) % 60:02d}"

        table = PrettyTable()
        table.field_names = ["Time", "Track"]
        if include_search_links:
            table.field_names += ["Search Link"]
        for track, timestamp in self.items():
            row = [format_timestamp(timestamp), track]
            if include_search_links:
                row += [f"https://ecosia.org/search?q={quote(str(track))}"]
            table.add_row(row)
        print(table)
