import smtplib
import sys
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("alinvelican@gmail.com", "hhazvynbviaytcsk")
 
msg = sys.argv[1]
server.sendmail("alinvelican@gmail.com", "dark_ride_dark_ride@yahoo.com", msg)
server.quit()