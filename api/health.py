import requests
from flask import Blueprint, current_app

from api.utils import (
    jsonify_data,
    url_for,
    get_jwt,
    jsonify_errors,
    get_response_data
)

health_api = Blueprint('health', __name__)


def check_health_abuse_ipdb_api():
    url = url_for('check')

    headers = {
        'Accept': 'application/json',
        'Key': get_jwt().get('key', '')
    }

    params = {
        'ipAddress': current_app.config.get('ABUSE_IPDB_HEALTH_CHECK_IP')
    }

    response = requests.get(url, headers=headers, params=params)

    return get_response_data(response)


@health_api.route('/health', methods=['POST'])
def health():
    response, errors = check_health_abuse_ipdb_api()

    if errors:
        return jsonify_errors(errors)

    return jsonify_data({'status': 'ok'})
