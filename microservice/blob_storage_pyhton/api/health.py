from flask import jsonify

from api import health_bp


@health_bp.route('/check', methods=['GET'])
def check():
    return jsonify(staus='Healthy')
