import logging
import os
import threading
from time import sleep

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

from ant_net_monitor.Status.cpu_status import CPUStatus, save_cpu_status
from ant_net_monitor.Status.ram_status import RAMStatus, save_ram_status

from .cli import init_db, init_db_command
from .extensions import db
from .Status.basic_status import BasicStatus, save_basic_status
from .status import status_bp


def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder="./dist/static",
        template_folder="./dist",
    )
    app.config.from_object("ant_net_monitor.config")

    # if test_config is None:
    #   # load the instance config, if it exists, when not testing
    #   app.config.from_pyfile("config.py", silent=True)
    # else:
    #   # load the test config if passed in
    #   app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/favicon.png")
    def fav():
        return send_from_directory(os.path.join(app.root_path, "dist"), "favicon.png")

    @app.route("/", defaults={"path": ""})
    @app.route("/<string:path>")
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    app.register_blueprint(status_bp)

    CORS(app)

    register_extensions(app)
    add_command(app)

    check_table_exist(app)

    set_basic_status_thread(app)
    set_cpu_status_thread(app)
    set_ram_status_thread(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)


def add_command(app):
    """Register Flask CLI commands."""
    app.cli.add_command(init_db_command)


# TODO 测试情况下的环境变量
def set_basic_status_thread(app):
    """Register basic status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_basic_status(BasicStatus())

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_cpu_status_thread(app):
    """Register cpu status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_cpu_status(CPUStatus())

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_ram_status_thread(app):
    """Register ram status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_ram_status(RAMStatus())
                sleep(1)

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def check_table_exist(app):
    """Check if `status` table exists."""
    with app.app_context():
        engine = db.get_engine()
        insp = db.inspect(engine)
        if "status" not in insp.get_table_names():
            init_db()
