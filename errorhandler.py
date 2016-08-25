
import json

class SmaError(object):
    
    def __init__(self, err_type, err_msg):
        self.err_type = err_type
        self.err_msg = err_msg
    
    def __str__(self):
        return json.dumps(
             {
                 "error": self.err_type
                 "message": self.err_msg
             }
            )

    def __lt__(self, other):
        if type(other) is SmaError:
            return self.err_type < other.err_type
        else:
            return self.err_type < other
    
    def __le__(self, other):
        if type(other) is SmaError:
            return self.err_type <= other.err_type
        else:
            return self.err_type <= other
    
    def __gt__(self, other):
        if type(other) is SmaError:
            return self.err_type > other.err_type
        else:
            return self.err_type > other
    
    def __ge__(self, other):
        if type(other) is SmaError:
            return self.err_type >= other.err_type
        else:
            return self.err_type >= other
    
    def __eq__(self, other):
        if type(other) is SmaError:
            return self.err_type is other.err_type
        else:
            return self.err_type is other
    
    def __ne__(self, other):
        if type(other) is SmaError:
            return self.err_type is not other.err_type
        else:
            return self.err_type is not other
    
    

def print_e(e):
    if type(e) is SmaError:
        return str(e)
    else:
        return json.dumps(
            {
            "error": 500
            "message": e
            }
        )
