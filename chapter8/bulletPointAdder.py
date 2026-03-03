# not import pyperclip, so using string
# import pyperclip

# get text from clipboard
# text = pyperclip.paste()

text = '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

#copy text to clipboard
#pyperclip.copy(text)
print(text)


