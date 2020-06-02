import psutil
from flask_restx import Namespace, Resource, fields

network = Namespace("network", description="Network statistics")

net_io_counters_model = network.model(
    "net_io_counters",
    {
        "bytes_sent": fields.Integer(description="number of bytes sent"),
        "bytes_recv": fields.Integer(description="number of bytes received"),
        "packets_sent": fields.Integer(description="number of packets sent"),
        "packets_recv": fields.Integer(description="number of packets received"),
        "errin": fields.Integer(description="total number of errors while receiving"),
        "errout": fields.Integer(description="total number of errors while sending"),
        "dropin": fields.Integer(
            description="total number of incoming packets which were dropped"
        ),
        "dropout": fields.Integer(
            description="total number of outgoing packets which were dropped (always 0 on macOS and BSD)"
        ),
    },
)

io_counters_nest = fields.Nested(net_io_counters_model)
io_counters_wild = fields.Wildcard(io_counters_nest)
net_io_counters_wild = network.model("net_io_counters_", {"*": io_counters_wild,})

net_if_stats_model = network.model(
    "net_if_stats",
    {
        "isup": fields.Boolean(
            description="a bool indicating whether the NIC is up and running."
        ),
        "duplex": fields.String(
            description="the duplex communication type; it can be either NIC_DUPLEX_FULL, NIC_DUPLEX_HALF or NIC_DUPLEX_UNKNOWN.",
            attribute=lambda x: x["duplex"].name,
        ),
        "speed": fields.Integer(
            description="the NIC speed expressed in mega bits (MB), if it can’t be determined (e.g. ‘localhost’) it will be set to 0."
        ),
        "mtu": fields.Integer(
            description="NIC’s maximum transmission unit expressed in bytes."
        ),
    },
)

if_stats_nest = fields.Nested(net_if_stats_model)
if_stats_wild = fields.Wildcard(if_stats_nest)
net_if_stats_wild = network.model("net_if_stats_", {"*": if_stats_wild,})

net_if_addrs_model = network.model(
    "net_if_addrs",
    {
        "family": fields.String(
            description="the address family, either AF_INET or AF_INET6 or psutil.AF_LINK, which refers to a MAC address.",
            attribute=lambda x: x["family"].name,
        ),
        "address": fields.String(description="the primary NIC address (always set)."),
        "netmask": fields.String(description="the netmask address (may be None)."),
        "broadcast": fields.String(description="the broadcast address (may be None)."),
        "ptp": fields.String(
            description="stands for “point to point”; it’s the destination address on a point to point interface (typically a VPN). broadcast and ptp are mutually exclusive. May be None."
        ),
    },
)

if_addrs_nest = fields.List(fields.Nested(net_if_addrs_model))
if_addrs_wild = fields.Wildcard(if_addrs_nest)
net_if_addrs_wild = network.model("net_if_addrs_", {"*": if_addrs_wild,})

network_model = network.model(
    "network_model",
    {
        "net_io_counters": fields.List(
            fields.Nested(
                net_io_counters_wild,
                description="Return system-wide network I/O statistics",
            )
        ),
        "net_if_stats": fields.List(
            fields.Nested(
                net_if_stats_wild,
                description="Return information about each NIC (network interface card) installed on the system as a dictionary whose keys are the NIC names",
            )
        ),
        "net_if_addrs": fields.List(
            fields.Nested(
                net_if_addrs_wild,
                description="Return the addresses associated to each NIC (network interface card) installed on the system as a dictionary whose keys are the NIC names and value is a list of named tuples for each address assigned to the NIC.",
            )
        ),
    },
)


@network.route("/network")
class Network(Resource):
    @network.marshal_with(network_model)
    def get(self):
        """Systems network stats.
        """
        return {
            "net_io_counters": {
                k: v._asdict() for (k, v) in psutil.net_io_counters(pernic=True).items()
            },
            "net_if_stats": {
                k: v._asdict() for (k, v) in psutil.net_if_stats().items()
            },
            "net_if_addrs": {
                k: [i._asdict() for i in v] for (k, v) in psutil.net_if_addrs().items()
            },
        }
