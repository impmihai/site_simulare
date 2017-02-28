#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import smtplib
import os

cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
first_name +=" " + last_name
email = form.getvalue('email')
mesaj = form.getvalue('mesaj')

text = "Nume: " + last_name + " Prenumele: " + first_name + " Email: " + email  + " Mesajul: " 

os.system("python /home/ddd/site-sim/site_simulare/site_simulare/cgi-bin/p.py " + str(text))


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Mesajul %s a fost trimis </h2>" % ( mesaj)
print "</body>"
print "</html>"