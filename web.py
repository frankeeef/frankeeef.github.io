file = open('index.html', 'w')

def text(text, heading):
    if heading == 'p':
        file.write('<p>' + text + '</p>')
    elif heading == 'h1':
        file.write('<h1>' + text + '</h1>')
    elif heading == 'h2':
        file.write('<h2>' + text + '</h2>')
    elif heading == 'h3':
        file.write('<h3>' + text + '</h3>')
    elif heading == 'h4':
        file.write('<h4>' + text + '</h4>')
    elif heading == 'h5':
        file.write('<h6>' + text + '</h5>')
    elif heading == 'h6':
        file.write('<h6>' + text + '</h6>')
def image(imagesrc, alt):
    file.write('<img src="' + imagesrc + '" alt="' + alt + '" />')
