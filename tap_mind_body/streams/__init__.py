from tap_mind_body.streams.classes import ClassesStream
from tap_mind_body.streams.class_visits import ClassVisitsStream
from tap_mind_body.streams.waitlist_entries import WaitlistEntriesStream


AVAILABLE_STREAMS = [
   ClassesStream,
   ClassVisitsStream,
   WaitlistEntriesStream,
]

__all__ = [s.__name__ for s in AVAILABLE_STREAMS]