import mysql.connector
import os
import matplotlib.pyplot as pt

# Configurations
from config import config
from dotenv import load_dotenv

load_dotenv()  # Imports environemnt variables from the '.env' file

# ===================SQL Connectivity=================

# SQL Connection
connection = mysql.connector.connect(
    host=config.get("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=config.get("DB_NAME"),
    port="3306",
    autocommit=config.get("DB_AUTOCOMMIT"),
)

cursor = connection.cursor(buffered=True)

# SQL functions


def checkUser(username, password=None):
    cmd = f"Select count(username) from login where username='{username}' and BINARY password='{password}'"
    cursor.execute(cmd)
    cmd = None
    a = cursor.fetchone()[0] >= 1
    return a


def human_format(num):
    if num < 1000:
        return num

    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000
    return "%.1f%s" % (num, ["", "K", "M", "G", "T", "P"][magnitude])


def updatePassword(username, sec_ans, sec_que, password):
    cmd = f"update login set password='{password}' where username='{username}' and sec_ans='{sec_ans}' and sec_que='{sec_que}' limit 1;"
    cursor.execute(cmd)
    cmd = f"select count(username) from login where username='{username}' and password='{password}' and sec_ans='{sec_ans}' and sec_que='{sec_que}';"
    cursor.execute(cmd)
    return cursor.fetchone()[0] >= 1


def updateUsername(oldusername, password, newusername):
    cmd = f"update login set username='{newusername}' where username='{oldusername}' and password='{password}' limit 1;"
    cursor.execute(cmd)
    cmd = f"select count(username) from login where username='{newusername}' and password='{password}''"
    cursor.execute(cmd)
    return cursor.fetchone()[0] >= 1


def find_g_id(name):
    cmd = f"select g_id from users where name = '{name}'"
    cursor.execute(cmd)
    out = cursor.fetchone()[0]
    return out


def checkin(g_id):
    cmd = f"select * from services where g_id = '{g_id}';"
    cursor.execute(cmd)
    reservation = cursor.fetchall()
    if reservation != []:
        subcmd = f"update services set check_in = curdate() where g_id = '{g_id}' "
        cursor.execute(subcmd)
        return "successful"
    else:
        return "No services for the given Guest"


def checkout(id):
    cmd = f"update services set check_out=current_timestamp where id={id} limit 1;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# ============Python Functions==========


def acceptable(*args, acceptables):
    """
    If the characters in StringVars passed as arguments are in acceptables return True, else returns False
    """
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True


# Get all users
def get_users():
    cmd = "select id, name, address, email_id, phone, created_at from users;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Add a user
def add_user(name, address, email_id, phone):
    cmd = f"insert into users(name,address,email_id,phone) values('{name}','{address}','{email_id}',{phone});"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# Get all services
def get_services():
    cmd = "select id, user_id,check_in,service, premium from services;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Get unique services
def get_unique_services():
    cmd = "select distinct service from services;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Get unique cities
def get_unique_cities():
    cmd = "select distinct address from users;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Get services count
def get_services_count(service):
    cmd = f"select count(id) from services where service = '{service}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


# Get city count
def get_city_count(city):
    cmd = f"select count(id) from users where address = '{city}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


# Add a reservation
def add_service(user_id, premium, service, check_in="now"):
    cmd = f"insert into services(user_id,check_in,service, premium) values('{user_id}',{f'{chr(39) + check_in + chr(39)}' if check_in != 'now' else 'current_timestamp'},'{service}','{premium}');"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# # Get all the user details
def get_total_users():
    cmd = "select count(id) from users;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


# Get total admins
def get_total_admins():
    cmd = "select count(username) from login;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


# Get services
def get_total_users_services():
    cmd = "select count(id) from services;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


def users():
    return get_total_users()


def services():
    return get_total_users_services()


def admins():
    return get_total_admins()


def delete_service(_id):
    cmd = f"delete from services where id='{_id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def delete_user(id):
    cmd = f"delete from users where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def update_users(name, address, id, phone):
    cmd = f"update users set address = '{address}',phone = {phone} , name = '{name}' where id = {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def update_services(id, user_id, check_in, service, premium):
    cmd = f"update services set check_in = '{check_in}',user_id = {user_id}, \
        service = '{service}',premium = '{premium}' where id= {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True

