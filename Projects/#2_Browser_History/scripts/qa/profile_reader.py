
from datetime import datetime
import os

def get_datetime():
    return datetime.now().strftime("%m_%d_%Y %H_%M_%S")

def change_profile_name():
    try:
        old_name = 'profile_output.txt'
        datetime_ = get_datetime()
        new_name = f'z_{datetime_}.txt'
        os.rename(old_name, new_name)
    except:
        old_name = 'qa\\profile_output.txt'
        datetime_ = get_datetime()
        new_name = f'qa\\z_{datetime_}.txt'
        os.rename(old_name, new_name)

if __name__ == "__main__":
    change_profile_name()
