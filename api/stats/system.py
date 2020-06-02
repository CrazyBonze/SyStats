import platform
import uuid
from datetime import datetime

from flask_restx import Namespace, Resource, fields
from uptime import boottime, uptime

system = Namespace("system", description="System information")

system_model = system.model(
    "system",
    {
        "system_id": fields.String(
            title="system_id", description=uuid.getnode.__doc__
        ),
        "uptime": fields.Float(
            title=uptime.__name__, description=uptime.__doc__
        ),
        "boottime": fields.DateTime(
            title=boottime.__name__, description=boottime.__doc__
        ),
        "system": fields.String(
            title=platform.system.__name__,
            description=platform.system.__doc__,
        ),
        "node": fields.String(
            title=platform.node.__name__,
            description=platform.node.__doc__,
        ),
        "release": fields.String(
            title=platform.release.__name__,
            description=platform.release.__doc__,
        ),
        "version": fields.String(
            title=platform.version.__name__,
            description=platform.version.__doc__,
        ),
        "machine": fields.String(
            title=platform.machine.__name__,
            description=platform.machine.__doc__,
        ),
        "processor": fields.String(
            title=platform.processor.__name__,
            description=platform.processor.__doc__,
        ),
    },
)


@system.route("/system")
class System(Resource):
    @system.marshal_with(system_model)
    def get(self):
        return {
            "system_id": uuid.getnode(),
            "uptime": uptime(),
            "boottime": boottime(),
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
        }
