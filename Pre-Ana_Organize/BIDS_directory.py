import os
import sys
if sys.version_info[0] >= 3:
    raise Exception("Must be using Python 2")

# This file creates a directory structure as denoted by
# the BIDS format. This program was designed in order to
# function with ACQ_convert.py and MAT_data.py
# (By default, script adds a matlab and biopac folder)

path = raw_input("Insert ABSOLUTE destination path for directory structure: ")
if path[-1:] == '/':
    path = path[:-1]
sub_count = raw_input("Insert number of subjects in study: ")
sets = raw_input("Insert number of sets (eg. subject one ran through two sets of stimuli): ")
print "Creating folders..."
subjects = list(xrange(int(sub_count)+1))
subjects.pop(0)  # remove subject 0 for BIDS formatting
for subject in subjects:
    if subject < 10:
        subject = '0' + str(subject)  # ensure 2 digit format
    else:
        subject = str(subject)
    # this makes the folder ex: ../sub01
    if not os.path.exists(path + "/sub" + subject):
        print "Creating directory tree for subject " + subject + "..."
        os.makedirs(path + "/sub" + subject)
    # this makes a sub folder ex: ../sub01/scr
    if not os.path.exists(path + "/sub" + subject + "/scr"):
        os.makedirs(path + "/sub" + subject + "/scr")
    # this makes a sub folder ex: ../sub01/bh
    if not os.path.exists(path + "/sub" + subject + "/bh"):
        os.makedirs(path + "/sub" + subject + "/bh")
    # this makes a sub folder ex: ../sub01/bh/sub01_A & sub01_B
    if not os.path.exists(path + "/sub" + subject + "/bh" + "/sub" + subject + "_A"):
        os.makedirs(path + "/sub" + subject + "/bh" + "/sub" + subject + "_A")
    if not os.path.exists(path + "/sub" + subject + "/bh" + "/sub" + subject + "_B"):
        os.makedirs(path + "/sub" + subject + "/bh" + "/sub" + subject + "_B")
    # this makes a sub folder ex: ../matlab_data
    if not os.path.exists(path + "/matlab_data"):
        os.makedirs(path + "/matlab_data")
    # this makes a sub folder ex: ../matlab_data/A & B
    if not os.path.exists(path + "/matlab_data" + "/A"):
        os.makedirs(path + "/matlab_data" + "/A")
    if not os.path.exists(path + "/matlab_data" + "/B"):
        os.makedirs(path + "/matlab_data" + "/B")
    # this makes a sub folder ex: ../matlab_data/A/sub01 & B/sub01
    if not os.path.exists(path + "/matlab_data" + "/A" + "/sub" + subject):
        os.makedirs(path + "/matlab_data" + "/A" + "/sub" + subject)
    if not os.path.exists(path + "/matlab_data" + "/B" + "/sub" + subject):
        os.makedirs(path + "/matlab_data" + "/B" + "/sub" + subject)
    # this makes a sub folder ex: ../Participant_Biopac_Data
    if not os.path.exists(path + "/Participant_Biopac_Data"):
        os.makedirs(path + "/Participant_Biopac_Data")
