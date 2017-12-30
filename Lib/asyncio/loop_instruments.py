"""Instrument base class."""

import abc


__all__ = 'LoopInstrument',


class LoopInstrument(abc.ABC):
    """Abstract base class for listening asyncio event loop signals."""

    def loop_start(self, loop):
        """Executed when the loop is started."""

    def tick_start(self, loop):
        """Executed at the begining of a new loop tick."""

    def io_start(self, loop, timeout):
        """Executed before start the IO process, receives the maximum
        waiting time desired."""

    def io_end(self, loop, timeout):
        """Executed when the IO process has finished, receives the maximum
        waiting time desired."""

    def tick_end(self, loop, handles):
        """Executed at the end of a loop tick, receives the number of handles
        executed within that tick"""

    def loop_stop(self, loop):
        """Executed when the loop is finished."""
