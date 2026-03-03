# 123-123-1234
def is_phone_number(text):
    is_phone_number = True;
    if len(text) == 12:
        for i, v in enumerate(text):
            if (i == 3 or i == 7) and v != '-':
                is_phone_number = False
            elif not v.isdigit():
                is_phone_number = False
    else:
        is_phone_number = False

    return is_phone_number