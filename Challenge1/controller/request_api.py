"""The Endpoints to manage the BID_REQUESTS"""
import json
from flask import  abort, request, Blueprint
from models import model as md
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprin  t for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/request', methods=['GET'])
def get_all_bids():
    """Return all bids
    @return: 200: an array of all known BIDS as a \
    flask/response object with application/json mimetype.
    """
    return_rows = md.get_bids()
    return json.dumps(return_rows)

@REQUEST_API.route('/request', methods=['POST'])
def create_bid():
    """Create a book request record
    @param userID: post : the user ID
    @param petID: post : the pet ID
    @param money: post : money bidding on
    @return: 200: a new_uuid as a flask/response object \
    with application/json mimetype.
    @raise 400: misunderstood request
    """
    print("Inside Create Bid")
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('userID'):
        abort(400)
    if not data.get('petID'):
        abort(400)
    if not data.get('money'):
        abort(400)
    md.insert_bid(data['petID'], data['userID'], data['money'])

    resp = {"status": "succeed"}
    resp_code = 200

    return json.dumps(resp),resp_code



