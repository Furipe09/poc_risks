def log_config():
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'INFO'
            }
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'INFO'
            }
        }
    }
    return LOGGING_CONFIG