import re

'''
() group
[] 字符区间
{} 量词，匹配多少个修饰符
 转移字符
| alternation operator,  or
? 0个或1个    非贪婪匹配
* 0个或多个
+ 一个或多个  
. 匹配除换行符外其他任何字符     re.compile('.*', re.DOTALL) 匹配所有
$               匹配结尾   
^  反向字符集     匹配开头  
r'bcat.*?b'
'''
# parentheses () define groups
def group_by_parentheses():
    phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo = phone_re.search('My phone number is 415-555-4242.')
    try:
        print(mo.group(1))
        print(mo.group(2))
        print(mo.group(0))
        print(mo.group())
        print(mo.groups())

        area_code, main_number = mo.groups()
        print(area_code, main_number)
    except AttributeError:
        print('No text matches')

#$ () * + - . ? [] \ ^ {} | needs to escape
def escape_in_regular():
    pattern = re.compile(r'(\(\d{3}\) (\d{3}-\d{4}))')
    mo = pattern.search('My phone number is (415) 555-4242')
    print(mo.group(1))
    print(mo.group(2))

# | alternation operator
def pipe_in_regular():
    pattern = re.compile(r'Cat(erpilar|astrophe|ch|egory)')
    mo = pattern.search('Catch me if you can, Caterpilar.')
    print(mo.group())
    print(mo.group(1))

#findall 如果有捕获组，只显示匹配的组
def find_all():
    pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    print(pattern.findall('Cell:548-123-4785 Work:212-555-0000'))

group_by_parentheses()
print('1-----------------')
escape_in_regular()
print('2-----------------')
pipe_in_regular()
print('3-----------------')
find_all()

pattern = re.compile(r'\bcat.*?\b')
print(pattern.findall('The cat found a catapult catalog in the catacombs.'))


