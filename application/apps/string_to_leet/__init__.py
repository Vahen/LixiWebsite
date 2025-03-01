import logging

from flask import Blueprint
from flask_restx import Api
from application.configuration import web_templates_dir, web_static_dir
from application.apps import apps_folder

logger = logging.getLogger("VahenWebsite.apps.stringToLeet")
string_to_leet_static_folder = web_static_dir + apps_folder + '/string_to_leet'
string_to_leet_template_folder = web_templates_dir + apps_folder + '/string_to_leet'

string_to_leet_bp = Blueprint('string_to_leet_bp', __name__,
                              static_folder=string_to_leet_static_folder,
                              template_folder=string_to_leet_template_folder,
                              url_prefix="/apps/string_to_leet")

string_to_leet_api = Api(string_to_leet_bp,
                         version="1.0",
                         title="String to Leet API",
                         description="The API for the String to leet app",
                         prefix="/api")

from application.apps.string_to_leet import routes
