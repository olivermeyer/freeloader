# freeloader

## Overview
Freeloader allows users to extract information about tracks in a DJ set recording.

Users can enter a link to a SoundCloud track; the app then downloads the track as mp3.
Alternatively, users can upload a mp3 directly.

After acquiring the mp3, the app allows users to set markers at specific times in the file.
These markers delineate tracks.

The app then splits the file into smaller parts based on the markers,
resulting in one file per track.

Each track is then further divided into 20-second segments (the optimal length can be determined later).
It passes a number of these segments to Shazam (or equivalent), and stores the information.

Finally, once each file has been processed, the app returns a list of time-based segments, together with
track information if available. It the track was not recognised, it is marked as such in the output.


Components
* Audio
  * Represents an audio segment
  * Can be split into parts
  * Recordings, Tracks and Parts are all Audio objects
