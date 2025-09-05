from typing import Annotated

from pydub import AudioSegment

Marker = Annotated[int, "Marker in milliseconds"]


class Audio:
    def __init__(self, segment: AudioSegment):
        """Initialize Audio with a pydub AudioSegment."""
        self.segment = segment

    def split(self, markers: list[Marker]) -> list["Audio"]:
        """Split the audio segment at the given markers."""
        if max(markers) > len(self.segment):
            raise ValueError("Marker exceeds audio segment duration")
        return [
            Audio(self.segment[start:end])
            for start, end in zip([0] + markers, markers + [len(self.segment)])
        ]
