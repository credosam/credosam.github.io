#!/usr/bin/python
import psycopg2
import config
from configparser import ConfigParser
 
 
def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
 
def connect(query='', is_select=False):
    """ Connect to the PostgreSQL database server """
    conn = None
    users = ()
    result = ''
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        if(is_select == True):
            result = cur.fetchall()
        else:
            result = cur.fetchone()[0]
            conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return result

def checkUsers(users,user,password):
    found_valid_user = False
    for each in users:
        print(each)
        print(each[1]+" : "+each[2])
        if(each[1] == user and each[2] == password):
            print("valid user found")
            found_valid_user = True
            break
    return found_valid_user
