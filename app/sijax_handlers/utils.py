import random
import string
import shutil
import errno


def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


def copyfiles(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def createzip(zipname, path):
    shutil.make_archive(zipname, 'zip', path)


def get_ntp_server(configuration_string):
    # Get the index of the first character that matches the find parameter
    ntp_from_index = configuration_string.find('ntp server')

    # Add 100 to that index to include the IP
    ntp_to_index = ntp_from_index + 100

    # Get the portion of the string, split it using the space character and return the third element.
    # Always will be the IP of the NTP Server
    return configuration_string[ntp_from_index:ntp_to_index].split(' ')[2]