from flask import Blueprint

blob_bp = Blueprint('blob', __name__, url_prefix='/blob')
health_bp = Blueprint('health', __name__, url_prefix='/health')
