import sys
import tempfile

import soundcloud
from audio import load, analyze
from models import Tracklist


def find_tracklist(url: str):
    track = soundcloud.resolve(url)
    with tempfile.NamedTemporaryFile(suffix='.mp3') as tmp_file:
        soundcloud.download(track, tmp_file.name)
        audio = load(tmp_file.name)
        tracks = analyze(audio)
        tracklist = Tracklist(
            sc_id=track.id,
            sc_url=url,
            sc_title=track.title,
            tracks=tracks,
        )
        tracklist.deduplicate().print()


if __name__ == "__main__":
    find_tracklist(sys.argv[1])
