#!/usr/bin/python

# This runs featquery across many subjects
# It requires user mods throughout; it also requires you to have made the mask
# before running the code. Also, if you run this more than once you will need
# to delete the featquery folders produced in each subjects folder

# Run via: ipython fsl-featquery.py

# Import necessary libraries
import os
import glob
import numpy as np
import pandas as pd
import csv

## Set Directories
basedir='/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'

## Group folders
grpdir=basedir+'/group/lvl3_A_shock/shock.gfeat/cope1.feat'
masknm='RIns_shock_mask_bmulbin' #no need for specifying .nii.gz
maskdir=grpdir #where's the mask?
maskin=maskdir+'/'+masknm+'.nii.gz'

## Info and Location of copes at participant lvl
modeldir='model001'
groupfeat='A_lvl2_v1.gfeat'

## Number of copedirs
# This assumes below that you have 10 copes per participant you're extracting
copenum=4

## List subjects
subs=sorted(glob.glob("%s/1[0-9][0-9][0-9][0-9]"%(basedir)))
#subs=sorted(glob.glob("%s/152[0-9][0-3,5-9]"%(basedir)))
#subs = ('15201',)

## Initial data dictionary for grp Results_basic
grpdic = {}

## Identify the ROI and labels you want to make masks of
for s in np.arange(0,len(subs)):
	subsplit=subs[s].split('/')
	sub=subsplit[-1]
	print(sub)
	grpdic[sub] = []
	## Directories
	datadir=basedir+'/'+sub+'/model/'+groupfeat
	## Find cope dirs
	copedirs=sorted(glob.glob("%s/cope[1-4].feat"%(datadir)))
	## Run featquery
	## Here you need to hardcode based on the cope dirs you are running
	os.system("featquery %s %s %s %s %s 1 stats/cope1 featquery-%s  -p -s %s" %(copenum, copedirs[0], copedirs[1], copedirs[2], copedirs[3], masknm, maskin))
#
	## Grab important info then save to text
	for cope in copedirs[0:copenum]:
		featqdir=cope+'/featquery-'+masknm
		df_name = featqdir+'/report.txt'
		#Load data as dataframe, mean %sigCG at [5]
		df = pd.read_csv(df_name, header=None, sep=' ')
		mean_effect=df[5][0]
		# Assign new label to datadic
		splitdir = cope.split('/')
		splitdir_cope = splitdir[-1][:-5]
		# Load data to dictionary
		grpdic[sub] = np.append(grpdic[sub],mean_effect)

# save to file
name=grpdir+'/'+masknm+'.csv'
# Save dictionary using strange code
header=['sub','CSmI', 'CSm', 'CSpI', 'CSpNoS']
#
keys = grpdic.keys()
with open(name,"w") as csv_file:
	writer = csv.writer(csv_file, keys, delimiter=",")
	writer.writerow(header)
	for key in keys:
		value=grpdic[key].tolist()
		writer.writerow([key,value[0],value[1],value[2],value[3]]) #Hardcode here
