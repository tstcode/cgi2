#!/usr/bin/python
import cgi, os

form = cgi.FieldStorage()
fileitem = form['myfile']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('/var/www/' + fn, 'wb').write(fileitem.file.read())

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h2>File Uploaded successfully...</h2><hr/>")
f=open(fn,'r')
data=f.read()
print("Content Uploaded is:",data)
print("</body></html>")
