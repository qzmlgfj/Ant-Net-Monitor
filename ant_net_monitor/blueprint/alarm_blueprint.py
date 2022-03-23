from flask import Blueprint, jsonify, request
from ..alarm.alarm_flag import AlarmFlag

alarm_bp = Blueprint("/api/alarm", __name__, url_prefix="/api/alarm")

@alarm_bp.route("alarm_flag", methods=["GET"])
def return_alarm_flag():
    return jsonify(AlarmFlag.get_all_flag())
