import psutil
from cpuinfo import get_cpu_info
from flask_restx import Namespace, Resource, fields

cpu = Namespace("cpu", description="CPU statistics")

cpu_times_model = cpu.model(
    "cpu_times",
    {
        "user": fields.Float(
            description="time spent by normal processes executing in user mode; on Linux this also includes guest time"
        ),
        "system": fields.Float(
            description="time spent by processes executing in kernel mode"
        ),
        "idle": fields.Float(description="time spent doing nothing"),
        "nice": fields.Float(
            description="time spent by niced (prioritized) processes executing in user mode; on Linux this also includes guest_nice time"
        ),
        "iowait": fields.Float(
            description="time spent waiting for I/O to complete. This is not accounted in idle time counter."
        ),
        "irq": fields.Float(description="time spent for servicing hardware interrupts"),
        "softirq": fields.Float(
            description="time spent for servicing software interrupts"
        ),
        "steal": fields.Float(
            description="time spent by other operating systems running in a virtualized environment"
        ),
        "guest": fields.Float(
            description="time spent running a virtual CPU for guest operating systems under the control of the Linux kernel"
        ),
        "guest_nice": fields.Float(
            description="time spent running a niced guest (virtual CPU for guest operating systems under the control of the Linux kernel)"
        ),
    },
)

cpu_freq_model = cpu.model(
    "cpu_freq", {"current": fields.Float, "min": fields.Float, "max": fields.Float}
)

cpu_model = cpu.model(
    "cpu",
    {
        "cpu_times": fields.Nested(
            cpu_times_model, description=psutil.cpu_times.__doc__
        ),
        "cpu_times_percent": fields.Nested(
            cpu_times_model, description=psutil.cpu_times_percent.__doc__
        ),
        "cpu_freq": fields.Nested(cpu_freq_model, description=psutil.cpu_freq.__doc__),
        "loadavg": fields.List(fields.Float, description=psutil.getloadavg.__doc__),
        "cpu_count": fields.Integer(description=psutil.cpu_count.__doc__),
    },
)

cpu_info_model = cpu.model(
    "cpu_info",
    {
        "python_version": fields.String(
            example="2.7.12.final.0 (64 bit)", description=""
        ),
        "cpuinfo_version": fields.List(fields.Integer(), example="", description=""),
        "hz_advertised": fields.String(example="2.9300 GHz", description=""),
        "hz_actual": fields.String(example="1.7330 GHz", description=""),
        "hz_advertised_raw": fields.List(fields.Integer(), example=[], description=""),
        "hz_actual_raw": fields.List(fields.Integer(), example=[], description=""),
        "arch": fields.String(example="X86_64", description=""),
        "bits": fields.Integer(example=64, description=""),
        "count": fields.Integer(example=4, description=""),
        "vendor_id": fields.String(example="GenuineIntel", description=""),
        "brand": fields.String(
            example="Intel(R) Xeon(R) CPU E5-2643 v2 @ 3.50GHz", description=""
        ),
        "stepping": fields.Integer(example=4, description=""),
        "model": fields.Integer(example=62, description=""),
        "extended_model": fields.Integer(example=3, description=""),
        "family": fields.Integer(example=6, description=""),
        "flags": fields.List(fields.String(), example=[], description=""),
        "l1_data_cache_size": fields.String(example="32 KiB", description=""),
        "l1_instruction_cache_size": fields.String(example="32 KiB", description=""),
        "l2_cache_size": fields.String(example="256 KiB", description=""),
        "l2_cache_line_size": fields.Integer(example=6, description=""),
        "l2_cache_associativity": fields.String(example="0x100", description=""),
        "l3_cache_size": fields.String(example="25600 KB", description=""),
    },
)


@cpu.route("/cpu")
class Cpu(Resource):
    @cpu.marshal_with(cpu_model)
    def get(self):
        """Systems CPU stats.
        """
        return {
            "cpu_times": psutil.cpu_times()._asdict(),
            "cpu_times_percent": psutil.cpu_times_percent(interval=1)._asdict(),
            "cpu_freq": psutil.cpu_freq()._asdict(),
            "loadavg": [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()],
            "cpu_count": psutil.cpu_count(),
        }


@cpu.route("/cpu/info")
class CpuInfo(Resource):
    @cpu.marshal_with(cpu_info_model)
    def get(self):
        """Returns the CPU info by using the best sources of information for your OS.
        """
        return get_cpu_info()
