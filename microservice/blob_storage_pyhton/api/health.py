from flask import jsonify, Blueprint, g

from api.base import Ok

health_bp = Blueprint('health', __name__, url_prefix='/health')


@health_bp.route('/check', methods=['GET'])
def check():
    return Ok(staus='Healthy')
