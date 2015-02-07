__author__ = 'mengpeng'

import logging

withlogger = logging.getLogger
getlogger = logging.getLogger

DEFAULT_LOGGING = {
    'disable_existing_loggers': False,
    'formatters': '%(asctime)s - %(levelname)s - %(message)s',
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler'
        }
    },
    'loggers': {
        'ggp': {
            'handlers': ['console', 'logfile']
        }
    }
}


def config_logging():
    logging.basicConfig(DEFAULT_LOGGING)