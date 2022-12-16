def error(msg):
    return {
        "status": "error",
        "data": msg
    }

def success(msg):
    return {
        "status": "ok",
        "data": msg
    }