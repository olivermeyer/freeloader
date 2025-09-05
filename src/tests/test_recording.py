import os

import tempfile

from pydub import AudioSegment
from pydub.generators import Sine


def generate_mp3() -> str:
    test_audio = Sine(440).to_audio_segment(duration=5000)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_path = temp_file.name
    test_audio.export(temp_path, format="mp3")
    yield temp_path
    os.remove(temp_path)


def test_recording_can_be_split_into_tracks(generate_mp3):
    audio = Sine(44100).to_audio_segment()
    with tempfile.TemporaryDirectory() as tmpdir:
        audio.export(tmpdir + "/test.mp3", format="mp3")
    recording = Recording(file="")
    tracks = recording.split(markers)
    assert len(tracks) == ...

