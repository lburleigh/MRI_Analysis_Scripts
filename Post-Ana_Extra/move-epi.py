#!/usr/bin/python

# This takes a target beta map and moves it to the grp folder
# then renames for given analysis,; for use with neurosynth or neurovault or PINES

# Execute via: ipython move-epi.py

import os
import glob
import numpy as np
import shutil


## Study directory
studydir = '/mnt/scratch-800/FCI'

## Set dir for files
datadir="%s/group/decoding-whole"%(studydir)

# Make dir for gropu decoding
if os.path.isdir("%s"%(datadir))==False:
	os.system("mkdir %s"%(datadir))

## Model name and task(block) name
model='model001'
phase='regulate'
copenum='2'
copename='csm'

## Find subject dirs
subdirs=glob.glob("%s/152[0-9][0-9]"%(studydir))
subdirs=glob.glob("%s/152[0-9][0-3,5-9]"%(studydir))


## Loop through each subject
for dirlist in list(subdirs):
	splitdir = dirlist.split('/')
	splitdir_sub = splitdir[-1]  # You may need to edit this
	subnum=splitdir_sub[:]    # You may need to edit this
	print(subnum)
	# Find source file
	src=glob.glob("%s/model/%s/%s.gfeat/cope%s.feat/stats/zstat1.nii.gz"%(dirlist,model,phase,copenum))
	#copy file
	dst=datadir+'/'+subnum+'-'+phase+'-'+copename+'.nii.gz'
	shutil.copy2(src[0],dst)
