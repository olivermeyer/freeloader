from src import soundcloud

if __name__ == "__main__":
    soundcloud.download(
        "https://soundcloud.com/rainbowdiscoclub/rdc-093-sound-metaphors-djs",
        "/tmp/test.mp3",
    )
