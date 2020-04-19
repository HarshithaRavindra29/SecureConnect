# SecureConnect
This is a hackathon project to detect NSFW content in a video stream.


# Installation
```
poetry install
```
Do note this does not install `opencv`, that has to be installed separately.

# Usage:
```
Usage:poetry run sfw [--tolerance=<tolerance>] [--debug]

Options:
--tolerance=<tolerance>   Number of video frames to tolerate before issuing a warning.[default=4]
--debug                   Prints the inference logs.
```
This will throw an exception `UnsafeEnvironment` if more than `tolerance` number of frames contain NSFW content.
