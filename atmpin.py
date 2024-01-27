def validate_atm_pin_code(pin):
    if(pin.isdigit()) and (len(pin)==4 or len(pin) == 6):
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")


pin = input()
validate_atm_pin_code(pin)