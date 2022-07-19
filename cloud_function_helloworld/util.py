from config import config

def format_greeting(name):
    msg = config['message']
    return msg.format(name)
