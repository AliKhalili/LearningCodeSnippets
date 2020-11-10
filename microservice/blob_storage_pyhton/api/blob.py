import os

from flask import request, g, Blueprint, send_file

from api.base import Ok, BadRequest
from data.model.meta_model import MetaModel
from data.repository import db
from helpers.configuration import configuration
from helpers.utils import random_generator

blob_bp = Blueprint('blob', __name__, url_prefix='/blob')


@blob_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        blob = file
        new_meta = MetaModel(file_name=file.filename,
                             key=random_generator(),
                             content_type=file.content_type,
                             content_disposition=file.content_type,
                             length=len(blob))
        db.add(new_meta)
        if db.save_change():
            try:
                with open(os.path.join(configuration.UPLOAD_FOLDER, 'temp', new_meta.id), 'wb') as file:
                    file.write(blob)
                return Ok(Key=new_meta.key)
            except Exception as exp:
                db.remove(new_meta.id)
                db.save_change()

    return BadRequest(Key=None)


@blob_bp.route('/download/<key>', methods=['GET'])
def download(key):
    meta = db.get(key)
    if meta:
        path = os.path.join(configuration.UPLOAD_FOLDER, 'temp', meta.id)
        if meta.path:
            path = os.path.join(configuration.UPLOAD_FOLDER, meta.path)
        return send_file(filename_or_fp=path,
                         as_attachment=True,
                         attachment_filename=meta.file_name,
                         mimetype=meta.content_type)
    return BadRequest()
