#!/usr/bin/python

# This creates the level1 fsf's from a template
# When making the template I use the Feat gui
# set it up with a sample participant
# after saving the .fsf file, find and replace
# the participant number with SUBNUM and run1 with
# runRUNNUM

# Execute via: ipython 4-bold-fsl-mk-lvl1.py

import os
import glob

## Study directory
#studydir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data'
studydir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'

## Set dir for fsf file
#fsfdir="%s/group/lvl1_B_feats_v4/time2"%(studydir)
fsfdir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses/group/lvl1_B_hab_feats_v1'
#lvl1_B_feats_v1'

## Set name of fsf template (you already created)
fsftemplate='lvl1_B'

## Model name and task(block) name
model='model001'
#func_name='task'
#task='train'

## Find subject dirs
subdirs=glob.glob("%s/1[0-9][0-9][0-9][0-9]"%(studydir))
#subdirs=glob.glob("%s/18301"%(studydir))
print(subdirs, studydir)

##########################################################################
## Loop through each subject
for dir in list(subdirs):
	splitdir = dir.split('/')
	splitdir_sub = splitdir[-1]  # You may need to edit this
	subnum=splitdir_sub[:]    # You may need to edit this
	#subnum = subdirs[-5:]
	print(subnum)
	subfiles=glob.glob("%s/func/B_hab_[0-9]_trrm.nii.gz"%(dir)) #assumes you ran vanilla feats already  
	for runnum in range(1,len(subfiles)+1):
		filein = fsfdir+'/'+fsftemplate+'.fsf' # fsf in name
		fileout = fsfdir+'/' +fsftemplate+'TEMP'+subnum+'-run'+str(runnum)+ '.fsf' #fsf out name
		replacements = {'17271':subnum,'run1':'run'+str(runnum),'hab_1':'hab_'+str(runnum)}
		with open("%s"%(filein), 'rb') as infile:
			with open("%s"%(fileout), 'w') as outfile:
				for line in infile:
					for src, target in replacements.iteritems():
						line=line.replace(src, target)
					outfile.write(line)
	## Run Condor and Feat  'RUNNUM':runnum
	#os.system("export FSLPARALLEL=condor")
	#os.system("feat %s" %(fileout))
