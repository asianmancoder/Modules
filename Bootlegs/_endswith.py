def _endswith(string, what):
    if string[len(string)-len(what):] == what:
        return True
    else:
        return False
