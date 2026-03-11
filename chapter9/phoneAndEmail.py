import pyperclip, re

phone_re = re.compile(r'''
    (\d{3}|\(\d{3}\))?   #区号
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext\.))\s*(\d{2,5})?
''', re.VERBOSE)

email_re = re.compile(r'''
    [\w.%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})
''', re.VERBOSE)

matches = []

text = pyperclip.paste()
for groups in phone_re.findall(text):
    phone_num = '-'.join(groups[1], groups[3], groups[5])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
        matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups)

if len(matches) > 0:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print('Copied to clipboard.')
else:
    print('No phone numbers or email addresses found.')
