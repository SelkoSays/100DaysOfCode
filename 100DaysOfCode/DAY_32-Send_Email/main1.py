##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas as pand

EMAIL = "dummy.mail32d@yahoo.com"
PASSWORD = "wpbgujuezmpjzokv"

now = dt.datetime.now()
today = (now.month,now.day)

data = pand.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for index, data_row in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    age = now.year - birthday_person["year"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    if "gmail" in EMAIL:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL,PASSWORD)
            if age%10 == 1  and age != 11:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}st Birthday!\n\n{contents}")
            elif age%10 == 2 and age != 12:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}nd Birthday!\n\n{contents}")
            elif age%10 == 3 and age != 13:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}rd Birthday!\n\n{contents}")
            else:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}th Birthday!\n\n{contents}")
    elif "yahoo" in EMAIL:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(EMAIL,PASSWORD)
            if age%10 == 1  and age != 11:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}st Birthday!\n\n{contents}")
            elif age%10 == 2 and age != 12:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}nd Birthday!\n\n{contents}")
            elif age%10 == 3 and age != 13:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}rd Birthday!\n\n{contents}")
            else:
                connection.sendmail(from_addr=EMAIL, to_addrs=birthday_person["email"],msg=f"Subject:Happy {age}th Birthday!\n\n{contents}")
