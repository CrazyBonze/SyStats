import psutil
from flask_restx import Namespace, Resource, fields

memory = Namespace("memory", description="Memory statistics")

virtual_memory_model = memory.model(
    "virtual_memory",
    {
        "total": fields.Integer(description="total physical memory (exclusive swap)."),
        "available": fields.Integer(
            description="the memory that can be given instantly to processes without the system going into swap. This is calculated by summing different memory values depending on the platform and it is supposed to be used to monitor actual memory usage in a cross platform fashion."
        ),
        "used": fields.Integer(
            description="memory used, calculated differently depending on the platform and designed for informational purposes only. total - free does not necessarily match used."
        ),
        "free": fields.Integer(
            description="memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the actual memory available (use available instead). total - used does not necessarily match free."
        ),
        "active": fields.Integer(
            description="memory currently in use or very recently used, and so it is in RAM."
        ),
        "inactive": fields.Integer(description="memory that is marked as not used."),
        "buffers": fields.Integer(
            description="cache for things like file system metadata."
        ),
        "cached": fields.Integer(description="cache for various things."),
        "shared": fields.Integer(
            description="memory that may be simultaneously accessed by multiple processes."
        ),
        "slab": fields.Integer(description="in-kernel data structures cache."),
        "wired": fields.Integer(
            description="memory that is marked to always stay in RAM. It is never moved to disk."
        ),
    },
)

swap_memory_model = memory.model(
    "swap_memory",
    {
        "total": fields.Integer(description="total swap memory in bytes"),
        "used": fields.Integer(description="used swap memory in bytes"),
        "free": fields.Integer(description="free swap memory in bytes"),
        "percent": fields.Integer(
            description="the percentage usage calculated as (total - available) / total * 100)"
        ),
        "sin": fields.Integer(
            description="the number of bytes the system has swapped in from disk (cumulative)"
        ),
        "sout": fields.Integer(
            description="the number of bytes the system has swapped out from disk (cumulative)"
        ),
    },
)

memory_model = memory.model(
    "memory",
    {
        "virtual_memory": fields.Nested(
            virtual_memory_model, description=psutil.virtual_memory.__doc__
        ),
        "swap_memory": fields.Nested(
            swap_memory_model, description=psutil.swap_memory.__doc__
        ),
    },
)


@memory.route("/memory")
class Memory(Resource):
    @memory.marshal_with(memory_model)
    def get(self):
        return {
            "virtual_memory": psutil.virtual_memory()._asdict(),
            "swap_memory": psutil.swap_memory()._asdict(),
        }
