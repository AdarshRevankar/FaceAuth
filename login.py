import pandas as pd
import re

df_db = pd.read_csv('data.csv', index_col=0)
df_db.iloc[:] = df_db[:].astype('str')


def check_credintial(uname, pswd):
    if (df_db['username'] == uname).any():
        if (df_db[df_db['username'] == uname]['password'] == pswd).any():
            return True
    return False


def create_new_account(uname, pswd):
    global df_db
    row = pd.DataFrame([[str(uname), str(pswd)]], columns=df_db.columns)
    df_db = df_db.append(row, ignore_index=True)
    df_db.to_csv('data.csv')
    print(df_db)


def check_username_existence(uname):
    return (df_db['username'] == uname).any()


def input_verification(username, password):
    return re.match(r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$', username) \
            and re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)

