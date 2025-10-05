from dataclasses import dataclass
from urllib.parse import quote

from prettytable import PrettyTable


@dataclass(frozen=True)
class TrackInfo:
    artist: str
    title: str

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"


@dataclass
class Tracklist:
    sc_id: int
    sc_url: str
    sc_title: str
    tracks: dict[int, TrackInfo]

    def add(self, timestamp: int, track: TrackInfo):
        """Add a track to the tracklist."""
        self.tracks[timestamp] = track

    def deduplicate(self):
        """Deduplicate the tracks in the tracklist."""
        track_to_earliest_timestamp = {}
        for timestamp, track in self.tracks.items():
            if track not in track_to_earliest_timestamp:
                track_to_earliest_timestamp[track] = timestamp
        self.tracks = {
            timestamp: track for track, timestamp in track_to_earliest_timestamp.items()
        }
        return self

    def print(self, include_search_links: bool):
        """Print the tracklist to stdout."""

        def format_timestamp(ms: int) -> str:
            return f"{ms // 3600000}:{(ms // 60000) % 60:02d}:{(ms // 1000) % 60:02d}"

        table = PrettyTable()
        table.field_names = ["Time", "Track"]
        if include_search_links:
            table.field_names += ["Search Link"]
        for timestamp, track in self.tracks.items():
            row = [format_timestamp(timestamp), track]
            if include_search_links:
                row += [f"https://ecosia.org/search?q={quote(str(track))}"]
            table.add_row(row)
        print(table)
        return self
