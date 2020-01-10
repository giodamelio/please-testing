from pprint import pprint
from src.add.lib import add

def handler(event, context):
    pprint(event)
    pprint(context)

    return {
        'result': add(event['a'], event['b'])
    }
