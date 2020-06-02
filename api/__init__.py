from flask import Blueprint
from flask_restx import Api

from api.stats.cpu import cpu
from api.stats.disk import disk
from api.stats.memory import memory
from api.stats.network import network
from api.stats.sensors import sensors
from api.stats.system import system

api = Api(
    Blueprint("api", __name__, url_prefix="/api"),
    # title='title',
    # version='1.0',
    # description='desc',
)

api.add_namespace(cpu, path="/stats")
api.add_namespace(memory, path="/stats")
api.add_namespace(disk, path="/stats")
api.add_namespace(network, path="/stats")
api.add_namespace(sensors, path="/stats")
api.add_namespace(system, path="/stats")
