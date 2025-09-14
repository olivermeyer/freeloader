# import tempfile
#
# from src import soundcloud
# from src.audio import Audio, analyze
#
#
# def test_download_split_and_analyze_audio():
#     tracklist = []
#     with tempfile.TemporaryDirectory() as tmpdir:
#         path = soundcloud.download(
#             "https://soundcloud.com/rainbowdiscoclub/rdc-093-sound-metaphors-djs",
#             f"{tmpdir}/raw.mp3",
#         )
#         audio = Audio.load(path)
#         tracks = audio.split([2000, 3000])
#         for track in tracks:
#             parts = track.split([1000])
#             for part in parts:
#                 tracklist.append(analyze(part))
