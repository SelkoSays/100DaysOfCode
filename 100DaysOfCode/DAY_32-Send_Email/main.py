"""
import smtplib
"""
g_email = "dummy.mail32d@gmail.com"
g_password = "8Zi&Z45%SK$i)YOv"
y_email = "dummy.mail32d@yahoo.com"
y_password = "wpbgujuezmpjzokv"
# actual y_pass = X8E7l+Nxp%#U88+
# gmail -> smtp.gmail.com
# yahoo -> smtp.mail.yahoo.com
# hotmail -> smtp.live.com
"""
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls() # Secure your connection -- tls = transport layer security
    connection.login(user=y_email,password=y_password)
    connection.sendmail(from_addr=y_email, to_addrs=g_email, msg="Subject:Hello\n\nThis is the body of my email.")
"""
"""
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1999,month=1,day=15)
print(date_of_birth)
"""
import smtplib
import datetime as dt
import random

now =  dt.datetime.now()
week_day = now.weekday()

if week_day == 1:
    with open("quotes.txt","r")as f:
        all_quotes = f.readlines()

    quote = random.choice(all_quotes)
    # From GOOGLE
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Secure your connection -- tls = transport layer security
        connection.login(user=g_email,password=g_password)
        connection.sendmail(from_addr=g_email, to_addrs=g_email, msg=f"Subject:Monday motivational quote\n\n{quote}")
    # From YAHOO
    """with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls() # Secure your connection -- tls = transport layer security
        connection.login(user=y_email,password=y_password)
        connection.sendmail(from_addr=y_email, to_addrs=g_email, msg=f"Subject:Monday motivational quote\n\n{quote}")"""