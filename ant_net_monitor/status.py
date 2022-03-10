from flask import Blueprint, jsonify

from .Status.cpu_status import get_last_cpu_status

from . import get_last_basic_status

status_bp = Blueprint("status", __name__, url_prefix="/status")

@status_bp.route("basic_status",methods=["GET"])
def return_basic_status():
    return jsonify(get_last_basic_status())

@status_bp.route("cpu_status",methods=["GET"])
def return_cpu_status():
    return jsonify(get_last_cpu_status())
