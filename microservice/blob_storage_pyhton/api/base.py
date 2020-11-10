import json

from flask import Response, g


def Ok(**kwargs):
    kwargs['Elapsed'] = g.request_time()
    return Response(json.dumps(kwargs), status=200, mimetype='application/json')


def BadRequest(**kwargs):
    kwargs['Elapsed'] = g.request_time()
    return Response(json.dumps(kwargs), status=400, mimetype='application/json')
