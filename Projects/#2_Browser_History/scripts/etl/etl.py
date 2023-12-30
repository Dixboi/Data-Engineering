
import pandas as pd
import numpy as np
import os

import json

from datetime import datetime

import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


#  Helper Functions
def error(skk):
    '''
    Produces a log that shows ERROR with the color red.
    ----
    Parameters
    skk: str - the line to display in red text.
    ----
    Return
    None
    '''
    logging.error("\033[91m {}\033[00m" .format(skk))


def debug(skk):
    '''
    Produces a log that shows DEBUG with the color yellow.
    ----
    Parameters
    skk: str - the line to display in yellow text.
    ----
    Return
    None
    '''
    logging.debug("\033[93m {}\033[00m" .format(skk))


def info(skk):
    '''
    Produces a log that shows INFO with the green red.
    ----
    Parameters
    skk: str - the line to display in green text.
    ----
    Return
    None
    '''
    logging.info("\033[92m {}\033[00m" .format(skk))


def helper_tpl(link):
    '''
    Simplifies the link. Removes the top-level domain and
    the scheme.
    ----
    Parameters
    link: str - the link to be processed
    ----
    Return
    website: str - the simplified link
    '''
    try:
        website = link.split('/')[2]
        website = website.split('.')

        if 'google' in website:
            website = f'Google {website[0].title()}'
        elif 'datacamp' in website:
            website = f'Datacamp'
        elif 'www' in website:
            website.remove('www')
            website = ' '.join(website[:-1]).title()
        else:
            website = ' '.join(website[:-1]).title()
    except Exception as e:
        error(f'{e} caught in execution. F: helper_tpl. L: {link}')
    else:
        info(f'{link} has been preprocessed.')
        return website


def helper_lls(file):
    '''
    Check if the "browser_history_local_data.csv" exists inside
    the directory.
    ----
    Parameters
    file: str - the file to check
    ----
    Return
    :bool
    '''
    try:
        is_file_exist = os.path.exists(file)
    except Exception as e:
        error(f'{e} caught in execution. F: helper_lls')
    else:
        info('File found.')
        return is_file_exist


#  Main etl functions
def extract_json(file='..\\data\\raw\\history.json'):
    '''
    Extract the json file that contains the details about
    browser history.
    ----
    Parameters
    file: str - the file path that contains the json file
    ----
    Return
    jfile: json - the json file
    '''
    try:
        with open(file, encoding='utf-8') as f:
            jfile = json.load(f)
    except FileNotFoundError as fe:
        debug(f'{fe} caught in execution.')
        return extract_json(file='..\\..\\data\\raw\\history.json')
    except Exception as e:
        error(f'{e} caught in execution. F: extract_json')
    else:
        info(f'Extracted the "history.json" file')
        return jfile


def extract_latest_timestamp():
    '''
    Extract the latest timestamp from a text file.
    ----
    Parameters
    None
    ----
    Return
    latest_time: float - the latest timestamp
    ----
    Example
    >>> extract_latest_timestamp()
    184024.313
    '''
    try:
        txt_file = open('..\\data\\raw\\latest_timestamp.txt', 'r')
    except FileNotFoundError as fe:
        debug(f'{fe} caught in execution.')
        txt_file = open('..\\..\\data\\raw\\latest_timestamp.txt', 'r')
        latest_time = float(txt_file.readlines()[0])
        return latest_time
    except Exception as e:
        error(f'{e} caught in execution. F: extract_latest_timestamp')
    else:
        info(f'Extracted latest timestamp.')
        latest_time = float(txt_file.readlines()[0])
        return latest_time


def transform_filter(jfile, latest_timestamp=0.0):
    '''
    Parses the json file to extract the needed information
    inside it: date, time, link, and title.
    ----
    Parameters
    jfile: file path - the path that contain the json file
    latest_timestamp: DEFAULT=0.0; float - the latest
        timestamp based on the latest link present from
        the json file.
    ----
    Return
    dates: list[Datetime] - list of datetimes from the json file
    times: float - the latest timestamp from the latest link on
        the json file
    links: list[str] - list of links from the json file
    titles: list[str] - list of titles from the json file
    ----
    Example
    >>> transform_filter('json.json', 100.0)
    ([12/27/2023, 9:39:54 PM], 150.0, ['www.sample.com'], ['Sample'])
    '''
    try:
        dates, times, links, titles = [], [], [], []
        for data in jfile:
            link = data['url']
            timestamp = data['lastVisitTimeTimestamp']
            if link.startswith('https') and timestamp > latest_timestamp:
                dates.append(data['lastVisitTime'])
                times.append(timestamp)
                links.append(link)
                titles.append(data['title'])
    except Exception as e:
        error(f'{e} caught in execution. F: transform_filter')
    else:
        info('Filtered needed data.')
        return dates, times[0], links, titles


def transform_preprocess_dates(dates):
    '''
    Preprocess datetimes. Split the date and time into
    different lists. The date should be in '%m/%d/%Y'
    format while the time should be in 30 minute intervals
    with 24-hour format.
    ----
    Parameters
    dates: list[Datetime] - list of datetimes to be processed
    ----
    Return
    dates_: list[Date] - list of dates
    times: list[str] - list of time intervals in 30-minute gap
    ----
    Example
    >>> transform_preprocess_dates(["12/27/2023, 9:39:54 PM"])
    ([12/27/2023], [21:30-21:59])
    '''
    try:
        dates_ = []
        times = []
        for date in dates:

            #  date
            splitted = date.split()
            d = splitted[0]
            d = d.replace(',', '')
            d = datetime.strptime(d, '%m/%d/%Y')
            d = d.date()
            dates_.append(d)

            #  time
            t = splitted[1]
            z = splitted[2]

            t_parts = t.split(':')
            hour = t_parts[0]
            minute = t_parts[1]

            if z == 'PM':
                hour = str((int(hour) + 12) % 24)

            time = ''
            if int(minute) < 30:
                time = f'{hour}:00-{hour}:29'
            else:
                time = f'{hour}:30-{hour}:59'

            times.append(time)
    except Exception as e:
        error(f'{e} caught in execution. F: transform_preprocess_dates')
    else:
        info('Preprocessed dates.')
        return dates_, times


def transform_preprocess_links(links):
    '''
    Preprocess links from the list of links.
    ----
    Parameters
    links: list[str] - list of links to preprocess
    ----
    Return
    websites: list[str] - list of preprocessed links
    '''
    try:
        websites = []
        for link in links:
            website = helper_tpl(link)
            websites.append(website)
    except Exception as e:
        error(f'{e} caught in execution. F: transform_preprocess_links.')
    else:
        info('Preprocessed all links.')
        return websites


def transform_preprocess_titles(titles):
    '''
    Remove the personal email from titles that contain it.
    ----
    Parameters
    titles: list[str] - list of website titles
    ----
    Return
    preprocessed_titles: list[str] - list of titles with removed
        email
    '''
    try:
        preprocessed_titles = []
        for title in titles:
            title = title.split()

            for index in range(len(title)):
                if '@gmail.com' in title[index]:
                    title.remove(title[index])
                    break
            preprocessed_titles.append(' '.join(title))
    except Exception as e:
        error(f'{e} caught in execution. F: transform_preprocess_titles.')
    else:
        info('Preprocessed titles.')
        return preprocessed_titles


def transform_to_df(dates_, times, websites, all_titles):
    '''
    Contain into a DataFrame all of the preprocessed data.
    ----
    Parameters
    dates_: list[Date] - list of preprocessed dates
    times: list[str] - list of preprocessed times
    websites: list[str] - list of preprocesssed websites
    all_titles: list[str] - list of preprocessed titles
    ----
    Return
    df: DataFrame - the dataframe that contains all the
        preprocessed data
    '''
    try:
        data = {
            'Date': dates_,
            'Time': times,
            'Website': websites,
            'Title': all_titles
        }
        df = pd.DataFrame(data)
    except Exception as e:
        error(f'{e} caught in execution. F: transform_to_df.')
    else:
        info('Data has been transformed into DataFrame.')
        return df


def transform_change_data_name(old_file, name):
    '''
    Change the history.json file into the latest timestamp.
    ----
    Parameters
    old_file: str - the file path to the history.json file
    name: str - the latest timestamp
    ----
    Return
    None
    '''
    try:
        new_file = f'..\\data\\raw\\z_{name}.json'
        os.rename(old_file, new_file)
    except FileNotFoundError as fe:
        debug(f'{fe} caught in execution.')
        old_file = '..\\..\\data\\raw\\history.json'
        name = name
        transform_change_data_name(old_file=old_file, name=name)
    except Exception as e:
        error(f'{e} caught in execution. F: transform_change_data_name.')
    else:
        info(f'Changed raw data (history.json) into {name}')


def load_new_latest_timestamp(file, new_time):
    '''
    Rewrite the latest timestamp based on the last timestamp on
    the data and write it as string. Save the file as
    "latest_timestamp.txt".
    ----
    Parameters
    new_time: float - latest timestamp
    ----
    Return
    None
    '''
    try:
        with open(file, 'w') as file:
            file.write(str(new_time))
    except FileNotFoundError as fe:
        debug(f'{fe} caught in execution.')
        new_time = new_time
        txt = '..\\..\\data\\raw\\latest_timestamp.txt'
        load_new_latest_timestamp(file=txt, new_time=new_time)
    except Exception as e:
        error(f'{e} caught in execution. F: load_new_latest_timestamp')
    else:
        info('Loaded new timestamp.')


def load_local_spreadsheet(df, timestamp):
    '''
    Load the DataFrame as a csv file and save it as
    "browser_history_local_data.csv". Append new values.
    Make a new file that contains the new batch of data
    and name the file based on the latest timestamp.
    ----
    Parameters
    df: DataFrame - the data to convert into csv
    timestamp: float - the latest timestamp
    ----
    Return
    None
    '''
    try:
        df.to_csv(f'..\\data\\preprocessed\\z_{timestamp}.csv', index=False)
        file = '..\\data\\preprocessed\\browser_history_local_data.csv'
        if helper_lls(file):
            df.to_csv(file, mode='a', index=False, header=False)
        else:
            df.to_csv(file, index=False)
    except Exception as e:
        error(f'{e} caught in execution. F: load_local_spreadsheet')
    else:
        info('Loaded to local spreadsheet.')


def load_cloud_spreadsheet(df):
    '''
    Load the DataFrame into Google Sheets.
    ----
    Parameters
    df: DataFrame - the DataFrame to be loaded
    ----
    Return
    None
    '''
    try:
        scope = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive"]
        json = 'path_to_google_credential.json' #  Change this one
        creds = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("name_of_spreadsheet") #  Change this one
        worksheet = spreadsheet.worksheet("name_of_sheet") #  Change this one
        info(f"Total iterates: {len(df['Date']) // 50 + 1}")
        info(f"Total links: {len(df['Date'])}")
        for row in range(len(df['Date'])):
            #  Send 50 data at max to avoid reaching the limit per minute.
            if row % 50 == 0:
                info("Sleep for 1 minute")
                time.sleep(60)
                info(f"Iterate {row + 1}")
            data = [str(df['Date'][row]),
                    str(df['Time'][row]),
                    str(df['Website'][row]),
                    str(df['Title'][row])]
            worksheet.append_row(data)
    except Exception as e:
        error(f'{e} caught in execution. F: load_cloud_spreadsheet')
    else:
        info('Loaded to cloud spreadsheet.')
