from flask import Blueprint, jsonify, request

from ..status import Status


status_bp = Blueprint("/api/status", __name__, url_prefix="/api/status")


@status_bp.route("basic_status", methods=["GET"])
def return_basic_status():
    return jsonify(Status.BasicStatus.get_last())


@status_bp.route("cpu_status", methods=["GET"])
def return_cpu_status():
    if request.args.get("type") == "init":
        return jsonify(Status.CPUStatus.get_batch())
    elif request.args.get("type") == "update":
        return jsonify(Status.CPUStatus.get_last())
    elif request.args.get("type") == "day":
        return jsonify(Status.CPUStatus.get_in_one_day())


@status_bp.route("ram_status", methods=["GET"])
def return_ram_status():
    if request.args.get("type") == "init":
        return jsonify(Status.RAMStatus.get_batch())
    elif request.args.get("type") == "update":
        return jsonify(Status.RAMStatus.get_last())
    elif request.args.get("type") == "day":
        return jsonify(Status.RAMStatus.get_in_one_day())


@status_bp.route("disk_status", methods=["GET"])
def return_disk_status():
    if request.args.get("type") == "init":
        return jsonify(Status.DiskStatus.get_batch())
    elif request.args.get("type") == "update":
        return jsonify(Status.DiskStatus.get_last())
    elif request.args.get("type") == "day":
        return jsonify(Status.DiskStatus.get_in_one_day())


@status_bp.route("network_status", methods=["GET"])
def return_network_status():
    if request.args.get("type") == "init":
        return jsonify(Status.NetworkStatus.get_batch())
    elif request.args.get("type") == "update":
        return jsonify(Status.NetworkStatus.get_last())
    elif request.args.get("type") == "day":
        return jsonify(Status.NetworkStatus.get_in_one_day())
