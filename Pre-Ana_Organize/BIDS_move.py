import os
import re
import csv
from distutils.dir_util import copy_tree
import sys
if sys.version_info[0] >= 3:
    raise Exception("Must be using Python 2")

#  This program reorganizes the CURRENT FOLDER into BIDS format
#  It makes assumptions:
#  1. Your participant folders are labelled with only participant numbers (i.e. 17271)
#  2. You want the BIDS folder right next to your data folder

ids = []
regex = '\d{5}'  # this is the regular expression for your participant numbers


# by default, looks for only a 5 digit number


def rename(path):
    global ids
    for root, folders, files in os.walk(path):
        for f in files:
            # first, handle all files in the current directory
            for i in range(len(ids)):  # note that i is starting at zero
                if i < 9:
                    num = "0" + str(i + 1)
                else:
                    num = str(i + 1)
                if ids[i] in f:
                    print "matched"
                    name = f.replace(ids[i], "sub" + num)  # now participant number is sub#
                    os.rename(path + '/' + f, path + '/' + name)
        for folder in folders:
            rename(path + '/' + folder)

            for i in range(len(ids)):  # note that i is starting at zero
                if i < 9:
                    num = "0" + str(i + 1)
                else:
                    num = str(i + 1)
                if ids[i] in folder:
                    name = folder.replace(ids[i], "sub" + num)  # now participant number is sub#
                    os.rename(path + '/' + folder, path + '/' + name)


copy_path = os.getcwd().rsplit('/', 1)[0] + "/my_dataset"
copy_tree(os.getcwd(), copy_path)  # make direct copy of directory tree right next to it

for folder in next(os.walk(os.getcwd()))[1]:
    if re.match(regex, folder) is not None:  # if the folder matches regex for our lab format (5 digit number)
        ids.append(int(folder))  # add each participant number to the id array
    else:
        print "fail"
ids.sort()
ids = [str(i) for i in ids]  # ids is now sorted and all ints for later concatenation

rename(copy_path)  # start the recursion on our BIDS output path

with open("conversion.csv", 'wb') as out:
    wr = csv.writer(out, quoting=csv.QUOTE_ALL)
    for i in range(len(ids)):
        wr.writerow([ids[i], "sub" + str(i)])
