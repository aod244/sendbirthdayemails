import pandas
import datetime as dt
import random
import smtplib

my_email = "put email here"
password = "put password here"
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row.tolist() for (index, data_row) in birthdays_df.iterrows()}
if (today_month, today_day) in birthdays_dict:
    letter_nr = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_nr}.txt", "r") as file:
        final_letter = file.readlines()
        replace_name = birthdays_dict[(today_month, today_day)][0]
        final_letter[0] = final_letter[0].replace("[NAME]", f"{replace_name}")
        send_address = birthdays_dict[(today_month, today_day)][1]
        final_letter = ''.join(final_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=send_address, msg=f"Subject:Happy Birthday!\n\n"
                                                                               f"{final_letter}")
