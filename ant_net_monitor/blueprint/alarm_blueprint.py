from flask import Blueprint, jsonify, request
from ..alarm.alarm import Alarm

alarm_bp = Blueprint("/api/alarm", __name__, url_prefix="/api/alarm")

@alarm_bp.route("alarm_item", methods=["GET"])
def return_alarm_flag():
    return jsonify(Alarm.get_all_alarm_items())

@alarm_bp.route("alarm_item", methods=["POST"])
def update_alarm_flag():
    alarm = request.get_json()
    print(alarm)
    try:
        Alarm.update_alarm(alarm)
    except Exception as e:
        return jsonify({"status": "fail"})
    return jsonify({"status": "success"})
