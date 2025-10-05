from prettytable import PrettyTable

from models import Tracklist

def format_timestamp(ms: int) -> str:
    return f"{ms//3600000}:{(ms//60000)%60:02d}:{(ms//1000)%60:02d}"


def display(tracklist: Tracklist):
    table = PrettyTable()
    table.field_names = ["Time", "Artist", "Title"]
    for timestamp, track in tracklist.tracks.items():
        table.add_row([format_timestamp(timestamp), track.artist, track.title])
    print(table)
