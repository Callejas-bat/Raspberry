import smtplib
import os
import urllib
from urllib.request import urlopen
import time
from datetime import datetime
import subprocess as sp


def whoiam():
    return sp.getoutput("who i am")


def final_ip(mensaje):
    numbers = []
    for a in str(mensaje):
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" or a == "0" or a == ".":
            numbers.append(a)
        else:
            pass
    ip_final = "".join(numbers)

    return ip_final


def ip_find():
    ip = urlopen("http://icanhazip.com").read()
    ip_real = str(ip)
    return ip


def ip_email(mensaje):
    CORREO = "correo"
    PASS = "pass"
    mensaje_def = "Subject: Ip Rasp\n" + str(mensaje) + "\n" + whoiam()
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(CORREO, PASS)
    server.sendmail(CORREO, CORREO, msg=mensaje_def)
    server.quit


def main():
    ip_check = None
    while True:
        if ip_check != ip_find:
            ip_check = ip_find
            ip_email(final_ip(ip_find()))
            print("+ Changed IP")
        else:
            pass

        if datetime.now().strftime('%H:%M') == '14:20' or datetime.now().strftime(
                '%H:%M') == '19:00' or datetime.now().strftime('%H:%M') == '16:00':
            ip_email(final_ip(ip_find()))
            print("||| " + final_ip(ip_find()) + " $Send it")
        else:
            pass

        time.sleep(60)


if __name__ == "__main__":
    main()
