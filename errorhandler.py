
import json

def print_e(e):
    return json.dumps(
      {
        "error": 500
        "message": e
      }
    )
