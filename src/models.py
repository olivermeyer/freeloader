from dataclasses import dataclass


@dataclass(frozen=True)
class TrackInfo:
    artist: str
    title: str


@dataclass
class Tracklist:
    sc_id: int
    sc_url: str
    sc_title: str
    tracks: dict[int, TrackInfo]

    def add(self, timestamp: int, track: TrackInfo):
        self.tracks[timestamp] = track

    def deduplicate(self):
        track_to_earliest_timestamp = {}
        for timestamp, track in self.tracks.items():
            if track not in track_to_earliest_timestamp:
                track_to_earliest_timestamp[track] = timestamp
        self.tracks = {timestamp: track for track, timestamp in track_to_earliest_timestamp.items()}
