import os

from flask import jsonify, request, g

from data.model.meta_model import MetaModel
from data.repository import db
from helpers.configuration import configuration
from helpers.utils import random_generator
from . import blob_bp


@blob_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        blob = file
        new_meta = MetaModel(file_name=file.filename, key=random_generator(), content_type=file.content_type,
                             content_disposition=file.content_type, length=len(blob))
        db.add(new_meta)
        if db.save_change():
            try:
                with open(os.path.join(configuration.UPLOAD_FOLDER, 'temp', new_meta.id), 'wb') as file:
                    file.write(blob)
                return jsonify(Key=new_meta.key, Elapsed=g.request_time)
            except Exception as exp:
                db.remove(new_meta.id)
                db.save_change()

    return jsonify(Key=None, Elapsed=g.request_time)
