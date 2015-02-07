__author__ = 'mengpeng'

import logging
import logging.config

withlogger = logging.getLogger
getlogger = logging.getLogger

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'precise': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'precise'
        },
        'logfile': {
            'filename': 'ggp.log',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'precise'
        }
    },
    'loggers': {
        'ggp': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        }
    }
}


def config_logging():
    logging.config.dictConfig(DEFAULT_LOGGING)