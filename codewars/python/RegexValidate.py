def validate_pin(pin):
    a = len(pin)
    valid_pin = pin.isdigit()
    if valid_pin == True:
        if a == 4 or a ==6:
            return True 
        else:
            return False 
    else:
        return False
