import config

def format_greeting(name):
    msg = config.config['greeting']
    return msg.format(name)
