from pathlib import Path
import os

with open('./aa.txt','a') as file:
    file.write('\nAppend text2')
with open('./aa.txt') as file:
    print(file.read())
