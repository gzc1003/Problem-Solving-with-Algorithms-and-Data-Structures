import re

html = '''<html>
               <head>
                  <title>
                     Example
                  </title>
               </head>

               <body><h1>
                  <h1>Hello, world</h1>
               </body>
          </html>'''

res = re.findall("<\w+>|</\w+>", html)
ltag = ['<html>', '<head>', '<title>', '<body>', '<h1>']
rtag = ['</html>', '</head>', '</title>', '</body>', '</h1>']


def match(tag1, tag2):
    index1 = ltag.index(tag1)
    index2 = rtag.index(tag2)
    return index1 == index2


stack = []
balanced = True

for tag in res:
    if tag in ltag:
        stack.append(tag)
    else:
        if len(stack) == 0:
            balanced = False
            break
        else:
            left_tag = stack.pop()
            if not match(left_tag, tag):
                balanced = False
                break

if len(stack) == 0 and balanced:
    print('True')
else:
    print('False')
