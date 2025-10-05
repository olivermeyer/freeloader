import tempfile

from pydub import AudioSegment
from tqdm import tqdm

from models import TrackInfo
from shazam import recognize

OFFSET = 30000
CHUNK_SIZE = 60000
SAMPLE_SIZE = 20000


class Audio:
    def __init__(self, segment: AudioSegment):
        """Initialize Audio with a pydub AudioSegment."""
        self.segment = segment

    def split(self, offset: int, chunk_size: int) -> list["Audio"]:
        """Split audio into chunks of given size."""
        chunks = []
        for i in range(offset, len(self.segment), chunk_size):
            chunks.append(Audio(self.segment[i:i+chunk_size]))
        return chunks

    def sample(self, size: int) -> "Audio":
        return Audio(self.segment[:size])


def load(path: str) -> "Audio":
    """Load an audio file from the given path."""
    print(f"Loading audio")
    return Audio(segment=AudioSegment.from_file(path))


def analyze(audio: Audio) -> dict[int, TrackInfo]:
    print(f"Analyzing:")
    tracks = {}
    with tempfile.NamedTemporaryFile(suffix='.mp3') as tmp_file:
        for i, chunk in enumerate(tqdm(audio.split(OFFSET, CHUNK_SIZE))):
            chunk.sample(SAMPLE_SIZE).segment.export(tmp_file.name)
            if track_info := recognize(tmp_file.name):
                time = OFFSET + i * CHUNK_SIZE
                tracks[time] = track_info
    return tracks
