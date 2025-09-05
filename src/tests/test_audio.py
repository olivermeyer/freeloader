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
