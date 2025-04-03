import os
import datetime
import pandas as pd

user=os.getlogin()

def now_time():
    now_date=datetime.datetime.now().strftime('%d.%m.%Y')
    return now_date
def sec():
    now_datetime=str(datetime.datetime.now()).split()
    current_time= now_datetime[1]
    return current_time


def loging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        if os.path.isfile('log.csv'):
            file_df = pd.read_csv('log.csv')
            data = {"id": [len(file_df)], "pc_username": [user], "function_name": [func_name],"Date": [now_time()],"Time":[sec()]}
            df = pd.DataFrame(data) 
            df.to_csv('log.csv', mode='a', index=False, header=False)
        else:
            data = {"pc_username": [user], "function_name": [func_name],"Date": [now_time()],"Time":[sec()]} 
            df = pd.DataFrame(data) 
            df.to_csv('log.csv')
        return result
    return wrapper