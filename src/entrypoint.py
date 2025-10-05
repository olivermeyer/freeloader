import argparse

import tempfile

import soundcloud
from audio import load, analyze
from models import Tracklist


parser = argparse.ArgumentParser()
parser.add_argument("url", help="SoundCloud URL")
parser.add_argument("-s", help="Include search links", action="store_true", default=False, dest="include_search_links")


def find_tracklist(url: str, include_search_links: bool):
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
        tracklist.deduplicate().print(include_search_links)


if __name__ == "__main__":
    args = parser.parse_args()
    find_tracklist(args.url, args.include_search_links)
