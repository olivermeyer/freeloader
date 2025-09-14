from dataclasses import dataclass
from typing import Annotated

from pydub import AudioSegment
from shazamio import Shazam

Marker = Annotated[int, "Marker in milliseconds"]


class Audio:
    def __init__(self, segment: AudioSegment, path: str | None = None):
        """Initialize Audio with a pydub AudioSegment."""
        self.segment = segment
        self.path = None

    def split(self, markers: list[Marker]) -> list["Audio"]:
        """Split the audio segment at the given markers."""
        if max(markers) > len(self.segment):
            raise ValueError("Marker exceeds audio segment duration")
        return [
            Audio(self.segment[start:end])
            for start, end in zip([0] + markers, markers + [len(self.segment)])
        ]

    @staticmethod
    def load(path: str) -> "Audio":
        """Load an audio file from the given path."""
        return Audio(segment=AudioSegment.from_file(path), path=path)


@dataclass
class TrackInfo:
    artist: str
    title: str


async def analyze(audio: Audio) -> TrackInfo | None:
    """Analyze the audio segment and return its properties."""
    shazam = Shazam()
    response = await shazam.recognize(audio.segment.raw_data)
    if "track" in response and response["track"]:
        return TrackInfo(
            artist=response["track"]["subtitle"],
            title=response["track"]["title"],
        )
