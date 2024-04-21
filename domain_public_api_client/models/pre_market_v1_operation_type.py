from enum import Enum


class PreMarketV1OperationType(str, Enum):
    ADD = "add"
    COPY = "copy"
    INVALID = "invalid"
    MOVE = "move"
    REMOVE = "remove"
    REPLACE = "replace"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
