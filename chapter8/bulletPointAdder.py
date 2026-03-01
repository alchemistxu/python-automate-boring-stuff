# not import pyperclip, so using string

text = '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

print(text)


