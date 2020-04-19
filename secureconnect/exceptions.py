UNSAFE_FRAMES_MESSAGE = "It seems to be unsafe to continue using your camera. Shutting down."


class UnsafeEnvironment(RuntimeError):
    def __init__(self, message, errors):
        super(UnsafeEnvironment, self).__init__(message)
        self.message = UNSAFE_FRAMES_MESSAGE
