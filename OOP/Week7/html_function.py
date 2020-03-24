def create_html(dict):
    html = '<!DOCTYPE html>\ <html> <head lang="en"> <meta charset="UTF-8"> <title>Tag Cloud Generator</title> </head> <body> <div style="text-align: center; width: 15%; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">'
    count = 0
    for key in dict.keys():
        html += '<span style="font-size: '
        html += str(dict[key]*10)
        html += 'px"> '
        html += key
        html += '</span>'
        count += 1
        if count % 4 == 0:
            html += '<br>'

    html += '</div> </body> </html>'
    fo = open("output.html", "w")
    fo.write(html)
