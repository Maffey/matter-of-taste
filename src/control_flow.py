class TooManyNumbersDetectedException(Exception):
    def __init__(self):
        super().__init__(
            "Too many numbers detected in the servings field. Cannot find which one means what."
        )
