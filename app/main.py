from flask import Flask, request, Response
from app.service import reverse_json
import json

app = Flask(__name__)


@app.route('/reverse', methods=['POST'])
def reverse():
    """
    Handler that parses the json body and provides it to the service method
    in charge of reversing the elements in the JSON
    :return: the dict returned by the service method as a JSON object
    """
    req_data = request.get_json()
    res = reverse_json(req_data)
    return Response(json.dumps(res), mimetype='application/json')


@app.errorhandler(400)
def bad_request(e):
    return error_response("Bad request", 400)


@app.errorhandler(404)
def page_not_found(e):
    return error_response("The resource was not found", 404)


@app.errorhandler(405)
def method_not_allowed(e):
    return error_response("The method is not allowed for the requested URL", 405)


@app.errorhandler(500)
def internal_server_error(e):
    return error_response("Internal server error", 500)


def error_response(message, error_code):
    res_body = {
        "message": message,
        "error_code": error_code
    }
    return Response(json.dumps(res_body), mimetype='application/json'), error_code
