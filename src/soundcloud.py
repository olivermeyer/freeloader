from dataclasses import dataclass

from sclib import SoundcloudAPI, Track


@dataclass
class SoundCloudTrack:
    id: int
    title: str
    url: str
    track: Track

    def write_mp3_to(self, file):
        """Write mp3 to file."""
        self.track.write_mp3_to(file)


def resolve(url: str) -> SoundCloudTrack:
    """Resolve a URL to a SoundCloudTrack object."""
    print(f"Resolving {url}")
    _track = SoundcloudAPI().resolve(url)
    return SoundCloudTrack(id=_track.id, title=_track.title, url=url, track=_track)


def download(track: SoundCloudTrack, path: str) -> str:
    """Download a SoundCloud track from the given URL to the specified path."""
    print(f"Downloading {track.id=} {track.title=}")
    with open(path, "wb+") as file:
        track.write_mp3_to(file)
    return path
