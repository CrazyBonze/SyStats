import psutil
from flask_restx import Namespace, Resource, fields

sensors = Namespace("sensors", description="Sensor statistics")


@sensors.route("/temps")
class Temps(Resource):
    def get(self):
        return str(psutil.sensors_temperatures())


@sensors.route("/fans")
class Fans(Resource):
    def get(self):
        return str(psutil.sensors_fans())


@sensors.route("/battery")
class Batery(Resource):
    def get(self):
        return str(psutil.sensors_battery())
