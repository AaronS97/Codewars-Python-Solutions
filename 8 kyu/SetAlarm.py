def set_alarm(employed, vacation):
    if employed: 
        if not vacation:
            return True
        else: 
            return False
    else:
        return False