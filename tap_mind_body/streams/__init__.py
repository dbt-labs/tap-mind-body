from tap_mind_body.streams.classes import ClassesStream
from tap_mind_body.streams.class_visits import ClassVisitsStream


AVAILABLE_STREAMS = [
   ClassesStream,
   ClassVisitsStream,
]

__all__ = [s.__name__ for s in AVAILABLE_STREAMS]
