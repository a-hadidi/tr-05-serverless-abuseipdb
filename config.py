import os

from version import VERSION


class Config(object):
    VERSION = VERSION

    SECRET_KEY = os.environ.get('SECRET_KEY', '')

    ABUSE_IPDB_API_CLIENT_VERSION = VERSION

    ABUSE_IPDB_API_URL = 'https://api.abuseipdb.com/api/v2/{endpoint}'

    ABUSE_IPDB_HEALTH_CHECK_IP = '192.168.1.100'

    ABUSE_IPDB_OBSERVABLE_TYPES = {
        'ip': 'IP',
        'ipv6': 'IPV6',
    }

    ABUSE_IPDB_SEARCH_PERIOD = 30

    ABUSE_SCORE_RELATIONS = {
        'Clean': (0, 25),
        'Suspicious': (26, 85),
        'Malicious': (86, 100)
    }

    CTIM_VERDICT_DEFAULTS = {
        'type': 'verdict',
    }

    CTIM_DISPOSITIONS = {
        'Clean': 1,
        'Suspicious': 3,
        'Malicious': 2
    }
