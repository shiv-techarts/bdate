#!/usr/bin/env python3

"""
#!//bin/ksh

# Shell Implementation

Date=$(/bin/date +%d-%b-%Y)

if [[ $1 != "" ]]; then
 cp -p $1 ${1}.${Date}.$$
fi
"""


class BDate:

    @staticmethod
    def date_pattern():
        """
            Return a date pattern
        :return: Day_MonthName_Year_HourMinSecMicrosecond
        """

        from datetime import datetime

        # Current time
        now = datetime.now()
        # Getting date
        date_val = now.strftime('%d_%b_%Y')
        # Getting hour:min:sec
        hour_val = now.strftime('%H%M%S')
        # Getting microsecond
        micro_val = now.strftime('%f')[:2]

        # Returns a str in described format
        return f'{date_val}_{hour_val}{micro_val}'

    @staticmethod
    def copy_file(file_name, new_file_name):
        """
            Copy one file to another
        :param file_name: file to be copied
        :param new_file_name: saved name copied file
        :return: None
        """

        import os

        if not os.path.exists(file_name):
            raise FileNotFoundError

        with open(str(file_name), 'rb') as infile:
            with open(str(new_file_name), 'wb') as outfile:
                while True:
                    buff = infile.read(10240)
                    if buff:
                        outfile.write(buff)
                    else:
                        break

        return


def create_backup_file(*args):
    """
       Takes the list of filenames and rename with date pattern in the end
    :param args: argument of file names
    :return: renames the file name[s] passed with added date_pattern
    """

    for file in list(*args):
        try:
            date_pattern = BDate.date_pattern()
            BDate.copy_file(file, f'{file}.{date_pattern}')
        except FileNotFoundError as err:
            print(f'[ERROR] {err.filename} : No such file or directory')


if __name__ == '__main__':
    """
        Takes the name/names of the file to rename with date_pattern
    :param None
    :return None
    """

    import sys

    if len(sys.argv) == 1:
        print("""Usage: bdate file_name""")
        exit(-1)

    # Removing script name from the list
    del sys.argv[0]

    # Calling the Main Command for creating filename with pattern
    create_backup_file(sys.argv)
