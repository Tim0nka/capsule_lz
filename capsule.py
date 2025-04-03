from datetime import datetime
import os
import pandas as pd


def logging(func):                          
    def wrapper(*args, **kwargs):
        usr_func = func
        org = func(*args, **kwargs)
        usr_func_name = str(usr_func.__name__)
        usr_name = os.getlogin()
        time_act = str(datetime.now().time())
        mounth_act =  str(datetime.now().date())
        logs = 'logs.csv'
        if os.path.isfile(logs):                                                                                          
            file_df = pd.read_csv(logs)
            data = {'': [len(file_df)], 'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[mounth_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv',header=False, index=False, mode='a')
        else:                                                                                                             
            data = {'User': [usr_name], 'Func': [usr_func_name], 'Time':[time_act], 'Date':[mounth_act]}
            df = pd.DataFrame(data)
            df.to_csv('logs.csv')
        return org
    return wrapper


@logging
def live():                                                                                                              
    print('Im live')

def main():

    live()

if __name__ == "__main__":
    main()