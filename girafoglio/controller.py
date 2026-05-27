from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TurnEvent(str, Enum):
    NEXT = "next"
    PREVIOUS = "previous"


@dataclass
class HeadMovementPageTurner:
    right_threshold: float = 25.0
    left_threshold: float = -25.0
    neutral_threshold: float = 10.0
    armed: bool = True

    def process_yaw(self, yaw: float) -> TurnEvent | None:
        if abs(yaw) <= self.neutral_threshold:
            self.armed = True
            return None

        if not self.armed:
            return None

        if yaw >= self.right_threshold:
            self.armed = False
            return TurnEvent.NEXT

        if yaw <= self.left_threshold:
            self.armed = False
            return TurnEvent.PREVIOUS

        return None
