from sclib import SoundcloudAPI


def download(url: str, path: str) -> str:
    """Download a SoundCloud track from the given URL to the specified path."""
    track = SoundcloudAPI().resolve(url)
    with open(path, "wb+") as file:
        track.write_mp3_to(file)
    return path
