"""Tests for loop_instruments.py."""

import unittest
from unittest import mock

import asyncio


class LoopInstrumentTests(unittest.TestCase):

    def test_methods(self):
        loop = mock.Mock()
        instrument = asyncio.LoopInstrument()
        self.assertEqual(instrument.loop_start(loop), None)
        self.assertEqual(instrument.tick_start(loop), None)
        self.assertEqual(instrument.io_start(loop, 0), None)
        self.assertEqual(instrument.io_end(loop, 0), None)
        self.assertEqual(instrument.tick_end(loop, 0), None)
        self.assertEqual(instrument.loop_stop(loop), None)


if __name__ == '__main__':
    unittest.main()
