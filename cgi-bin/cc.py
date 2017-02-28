#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import smtplib
import os
import smtplib
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
first_name +=" " + last_name
email = form.getvalue('email')
mesaj = form.getvalue('mesaj')
p = str("\nprenume: ")
n = str("\nnume: ")
m = str("\nmesaj: ")
pp = str(first_name)
nn = str(last_name)
mm = str(mesaj)

ee = str(email)
e = str("email ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("alinvelican@gmail.com", "hhazvynbviaytcsk")
server.sendmail("alinvelican@gmail.com", "dark_ride_dark_ride@yahoo.com",   n + nn + p + pp + e+ ee+ m + mm)
server.quit()


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Mesajul %s a fost trimis </h2>" % ( mesaj)
print "</body>"
print "</html>"