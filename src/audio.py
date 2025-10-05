import tempfile

from pydub import AudioSegment
from tqdm import tqdm

from models import TrackInfo
from shazam import recognize
from src.types import TimeInMs

OFFSET: TimeInMs = 30000
CHUNK_SIZE: TimeInMs = 60000
SAMPLE_SIZE: TimeInMs = 20000


class Audio:
    def __init__(self, segment: AudioSegment):
        """Initialize Audio with a pydub AudioSegment."""
        self.segment = segment

    def split(self, offset: TimeInMs, chunk_size: TimeInMs) -> list["Audio"]:
        """Split audio into chunks of given size."""
        chunks = []
        for i in range(offset, len(self.segment), chunk_size):
            chunks.append(Audio(self.segment[i : i + chunk_size]))
        return chunks

    def sample(self, size: TimeInMs) -> "Audio":
        """Sample audio with given size."""
        return Audio(self.segment[:size])

    def export(self, path: str):
        """Export audio to given path."""
        self.segment.export(path)


def load(path: str) -> "Audio":
    """Load an audio file from the given path."""
    print("Loading audio")
    return Audio(segment=AudioSegment.from_file(path))


def analyze(audio: Audio) -> list[tuple[TrackInfo, TimeInMs]]:
    """Analyze the given audio."""
    print("Analyzing:")
    tracks = []
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp_file:
        for i, chunk in enumerate(tqdm(audio.split(OFFSET, CHUNK_SIZE))):
            chunk.sample(SAMPLE_SIZE).export(tmp_file.name)
            if track_info := recognize(tmp_file.name):
                time = OFFSET + i * CHUNK_SIZE
                tracks.append((track_info, time))
    return tracks
