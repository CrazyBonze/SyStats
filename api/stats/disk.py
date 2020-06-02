import psutil
from flask_restx import Namespace, Resource, fields

disk = Namespace("disk", description="Disk statistics")

io_counters_model = disk.model(
    "io_counters",
    {
        "read_count": fields.Integer(description="number of reads"),
        "write_count": fields.Integer(description="number of writes"),
        "read_bytes": fields.Integer(description="number of bytes read"),
        "write_bytes": fields.Integer(description="number of bytes written"),
        "read_time": fields.Integer(
            description="time spent reading from disk (in milliseconds)"
        ),
        "write_time": fields.Integer(
            description="time spent writing to disk (in milliseconds)"
        ),
        "busy_time": fields.Integer(
            description="time spent doing actual I/Os (in milliseconds)"
        ),
        "read_merged_count": fields.Integer(description="number of merged reads"),
        "write_merged_count": fields.Integer(description="number of merged writes"),
    },
)

nest = fields.Nested(io_counters_model)
wild = fields.Wildcard(nest)
io_counters_wild = disk.model("io_counters_", {"*": wild,})

disk_usage_model = disk.model(
    "disk_usage",
    {
        "total": fields.Integer,
        "used": fields.Integer,
        "free": fields.Integer,
        "percent": fields.Float,
    },
)

disk_partitions_model = disk.model(
    "disk_partitions",
    {
        "device": fields.String,
        "mountpoint": fields.String,
        "fstype": fields.String,
        "opts": fields.String,
    },
)


disk_model = disk.model(
    "disk_model",
    {
        "io_counters": fields.Nested(
            io_counters_wild, description="Return system-wide disk I/O statistics"
        ),
        "disk_usage": fields.Nested(
            disk_usage_model,
            description="Return disk usage statistics about the partition which contains the given path as a named tuple including total, used and free space expressed in bytes, plus the percentage usage.",
        ),
        "disk_partitions": fields.List(
            fields.Nested(
                disk_partitions_model,
                description="Return all mounted disk partitions as a list of named tuples including device, mount point and filesystem type, similarly to “df” command on UNIX.",
            )
        ),
    },
)


@disk.route("/disk")
class Disk(Resource):
    @disk.marshal_with(disk_model)
    def get(self):
        return {
            "io_counters": {
                k: v._asdict()
                for (k, v) in psutil.disk_io_counters(perdisk=True).items()
            },
            "disk_usage": psutil.disk_usage("/")._asdict(),
            "disk_partitions": [p._asdict() for p in psutil.disk_partitions()],
        }
