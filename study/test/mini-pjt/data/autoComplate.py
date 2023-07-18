import pyscript
import re


def showList(data, value, nowIndex):
    p = re.compile(f'([{value}])')
    result = ""

    for i, v in enumerate(data):
        #print(i,v)
        result += '<div class="'
        result += 'active">' if nowIndex == i else '">'
        result += p.sub(r'<mark>\1</mark>', v) + '</div>'
    
    pyscript.autoComplete.innerHTML = result
