"""
Usage: sfw [--tolerance=<tolerance>] [--debug]

Options:
--tolerance=<tolerance>   Number of video frames to tolerate before issuing a warning.[default=4]
--debug                   Prints the inference logs.
"""
from collections import deque
import cv2

from docopt import docopt
from nudenet import NudeClassifier
from secureconnect import inference
from secureconnect.exceptions import UnsafeEnvironment


# load the model once for every inference.
mdl = NudeClassifier()


def is_safety_buffer_critical(queue, tolerance):
    """
    Exit program with an error.

    If all items in the queue are True. This means we
    have exhausted our tolerance for nsfw content and it
    is unsafe for continuing to use video-source.
    """
    unsafe_flags = [item for item in list(queue) if item]
    if unsafe_flags == tolerance:
        raise UnsafeEnvironment


def reset_safety_buffer_if_stale(queue, tolerance):
    """
    Reset the buffer.

    If n - 1, items in the queue containing max n items
    are False, we can clear the queue.

    NAIVE: We are also clearing the one True case this
    function receives.
    """
    consecutive_safe = [item for item in list(queue)[:3] if not item]
    if len(consecutive_safe) == tolerance - 1:
        queue.clear()


def main():
    args = docopt(__doc__)
    debug = args["--debug"]
    video = cv2.VideoCapture(0)
    image_label = "__NSFW_SCAN__.jpg"
    label = "unsafe"
    tolerance = int(args["--tolerance"]) or 4
    safety_buffer = deque(maxlen=tolerance)
    while True:
        _, frame = video.read()
        cv2.imwrite(image_label, frame)
        not_safe = inference.run(mdl, image_label, debug=debug)\
                            .get(image_label)\
                            .get(label) >= 0.6

        safety_buffer.append(not_safe)
        if debug:
            print(safety_buffer)
        is_safety_buffer_critical(safety_buffer, tolerance)
        reset_safety_buffer_if_stale(safety_buffer, tolerance)
