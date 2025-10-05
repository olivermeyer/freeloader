import asyncio

from shazamio import Shazam

from models import TrackInfo


def recognize(path: str) -> TrackInfo:
    return asyncio.run(recognize_async(path))


async def recognize_async(path: str) -> TrackInfo | None:
    """Analyze the audio segment and return its properties."""
    shazam = Shazam()
    response = await shazam.recognize(path)
    # TODO: use serialized TrackInfo https://github.com/shazamio/ShazamIO?tab=readme-ov-file#how-to-use-data-serialization
    if "track" in response and response["track"]:
        return TrackInfo(
            artist=response["track"]["subtitle"],
            title=response["track"]["title"],
        )
    return None
