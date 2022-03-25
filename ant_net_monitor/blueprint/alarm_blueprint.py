from flask import Blueprint, jsonify, request
from ..alarm.alarm import Alarm

alarm_bp = Blueprint("/api/alarm", __name__, url_prefix="/api/alarm")

@alarm_bp.route("alarm_item", methods=["GET"])
def return_alarm_flag():
    return jsonify(Alarm.get_all_alarm_items())
