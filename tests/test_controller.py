import unittest

from girafoglio import HeadMovementPageTurner, TurnEvent


class HeadMovementPageTurnerTest(unittest.TestCase):
    def test_turns_next_on_right_threshold(self):
        turner = HeadMovementPageTurner()
        self.assertEqual(turner.process_yaw(30), TurnEvent.NEXT)

    def test_turns_previous_on_left_threshold(self):
        turner = HeadMovementPageTurner()
        self.assertEqual(turner.process_yaw(-30), TurnEvent.PREVIOUS)

    def test_requires_return_to_neutral_before_new_turn(self):
        turner = HeadMovementPageTurner()
        self.assertEqual(turner.process_yaw(30), TurnEvent.NEXT)
        self.assertIsNone(turner.process_yaw(35))
        self.assertIsNone(turner.process_yaw(0))
        self.assertEqual(turner.process_yaw(30), TurnEvent.NEXT)


if __name__ == "__main__":
    unittest.main()
