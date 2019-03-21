import re

def parse_markdown(markdown):
    lines = markdown.split('\n')
    result = ''
    in_list = False

    for i in lines:
        # parse headers of various lengths with regex (only checks h1, h2 & h6)
        for pattern in ('###### (.*)', '## (.*)', '# (.*)'):
            if(re.match(pattern, i)):
                i = "<h" + str(len(pattern) - 5) + ">" + i[(len(pattern)-4):] + "</h" + str(len(pattern) - 5) + ">"

        if re.match(r'\* (.*)', i):
            curr = re.match(r'\* (.*)', i).group(1)
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if not in_list:
                in_list = True
                if m1:
                    curr = m1.group(1) + '<strong>' + m1.group(2) + '</strong>' + m1.group(3)
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + '</em>' + m1.group(3)
                i = '<ul><li>' + curr + '</li>'
            else:
                i = '<li>' + re.match(r'\* (.*)', i).group(1) + '</li>'
            if m1:
                curr = m1.group(1) + '<strong><em>' + m1.group(2) + '</strong></em>' + m1.group(3)
        else:
            if in_list:
                i = '</ul>+i'
                in_list = False

        if not re.match('<h|<ul|<p|<li', i):
            i = '<p>' + i + '</p>'
        match = re.match('(.*)__(.*)__(.*)', i)
        if match:
            i = match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)
        match = re.match('(.*)_(.*)_(.*)', i)
        if match:
            i = match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)
        result += i
    if in_list:
        result += '</ul>'
    return result
