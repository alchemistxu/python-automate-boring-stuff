# 123-123-1234
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i, v in enumerate(text):
        if i==3 or i==7:
            if v != '-':
                return False
        else:
            if not v.isdigit():
                return False
    return True

def found_phone_number():
    message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    for i in range(len(message)):
        segment = message[i:i+12]
        if is_phone_number(segment):
            print('Found phone number: ' + segment)

#print(is_phone_number('123-584-2543'))
found_phone_number()
