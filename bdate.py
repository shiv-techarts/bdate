#!/usr/bin/env python3


def date_pattern():
    """
        Return the date pattern
    params: None
    return: YearMonthDay_HourMinSecMicroSecond
    """

    from datetime import datetime

    # Current time
    now = datetime.now()
    # Getting date
    date_val = now.strftime('%Y%m%d')
    # Getting hour:min:sec
    hour_val = now.strftime('%H%M%S')
    # Getting microsecond
    micro_val = now.strftime('%f')[:2]

    # Returns a str in described format
    return f'{date_val}_{hour_val}{micro_val}'


def main(*args):
    """
       Takes the list of filenames and rename with date pattern in the end 
    params: variable argument of file names
    return: renames the file name[s] passed with added date_pattern
    """

    import os

    for file in list(*args):
        try:
            os.rename(file, f'{file}_{date_pattern()}')
        except FileNotFoundError as err:
            print(f'[ERROR] {err.filename} : No such file or directory')


if __name__ == '__main__':
    """
        Takes the name/names of the file to rename with date_pattern
    params: None
    return: None
    """

    import sys

    if len(sys.argv) == 1:
        print("""Usage: bdate file_name""")
        exit(-1) 

    # Removing script name from the list
    del sys.argv[0]

    # Calling the Main Command for creating filename with pattern
    main(sys.argv)
