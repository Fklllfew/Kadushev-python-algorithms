def prison(word, tag):
    tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div',
            'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
    if tag in tags:
        return f"<{tag}>{word}</{tag}>"
    else:
        return 'Введён неверный тег'

tag = input()
string = input()
print(prison(string, tag))