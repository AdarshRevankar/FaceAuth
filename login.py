import pandas as pd

df_db = pd.read_csv('data.csv')


def check_credintial(uname, pswd):
    if df_db['username'][0] == uname:
        if df_db[df_db['username']]['password'] == pswd:
            return True
    return False


def insert_new(uname, pswd):
    df_db.insert([uname, pswd])