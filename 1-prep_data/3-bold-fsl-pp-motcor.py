#!/usr/bin/env python

# Script for running FSL motion correction
# It's run with the framewise displacement option thres 0.9 per Siegel et al. 2014 HBM
#
# ipython bold-fsl-pp-motcor.py

import numpy as np
import os
import glob

## Study directory
studydir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'

##
phase='hab_B'

# Name html file to put all QA info together.
outhtml = studydir+'/group/bold_motion_QA_'+phase+'.html'
outpdf = studydir+'/group/bold_motion_QA_'+phase+'.pdf'

## Delete previous output fsl_motion_outliers
#os.system("rm %s"%(out_bad_bold_list))
#os.system("rm %s"%(outhtml)) #need to move

## Find raw EPI nii files
subdirs=glob.glob('%s/1[0-9][0-9][0-9][0-9]/func/B_hab_[1-9]_trrm.nii.gz'%(studydir))
#subdirs=glob.glob("%s/18301/func/A_task_[1-9]_trrm.nii.gz"%(studydir))


for cur_bold in subdirs:
	print(cur_bold)
	#Current directory
	curdir = os.path.dirname(cur_bold)
	# QA file for flagging potential bad subjects
	out_bad_bold_list = studydir+'group/subsgt20_vol_scrub-'+phase+'.txt'
	#Strip .nii.gz (FSL doesn't want the file ext)
	cur_bold_no_nii = cur_bold[:-7]
	# Strip dir stuff to isolate phase and run
	fname=cur_bold_no_nii[len(curdir)+1:]
	# Make dir for motion assessments
	if os.path.isdir("%s/motion_assess"%(curdir))==False:
		os.system("mkdir %s/motion_assess"%(curdir))
	#Run fsl_motion_outlier
	os.system("fsl_motion_outliers -i %s -o %s/motion_assess/confound-%s.txt --fd --thresh=0.9 -p %s/motion_assess/fd_plot-%s -v > %s/motion_assess/outlier_output-%s.txt"%(cur_bold_no_nii, curdir, fname, curdir, fname, curdir, fname))
	# If no confounds create blank confound for easier scripting later
	if os.path.isfile("%s/motion_assess/confound-%s.txt"%(curdir,fname))==False:
		os.system("touch %s/motion_assess/confound-%s.txt"%(curdir,fname))
	# Put confound info into html file for review later on
	os.system("cat %s/motion_assess/outlier_output-%s.txt >> %s"%(curdir,fname, outhtml))
	os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s/motion_assess/fd_plot-%s.png WIDTH=100%s></BODY></HTML>' >> %s"%(curdir, curdir, fname,'%', outhtml))


## Convert html to pdf
os.system("pandoc %s -o %s"%(outhtml,outpdf))
