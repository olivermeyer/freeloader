import tempfile
from typing import Generator

import pytest
from pydub.generators import Sine

from src.audio import Audio


def test_audio_can_split_segment_into_parts():
    audio = Audio(segment=Sine(44100).to_audio_segment(duration=5))
    parts = audio.split([2, 3])
    assert len(parts) == 3
    assert round(parts[0].segment.duration_seconds, 3) == 0.002
    assert round(parts[1].segment.duration_seconds, 3) == 0.001
    assert round(parts[2].segment.duration_seconds, 3) == 0.002


def test_audio_cannot_split_segment_beyond_duration():
    audio = Audio(segment=Sine(44100).to_audio_segment(duration=0))
    with pytest.raises(ValueError):
        audio.split([2])


@pytest.fixture
def mp3() -> Generator[str, None, None]:
    audio = Sine(440).to_audio_segment(duration=5)
    with tempfile.NamedTemporaryFile(suffix=".mp3") as fh:
        path = fh.name
        audio.export(path, format="mp3")
        yield path


def test_audio_can_load_local_file(mp3):
    audio = Audio.load(mp3)
    assert round(audio.segment.duration_seconds, 3) == 0.005
