#!/usr/bin/env python
import glob
import os
 
 
path = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'
 
#subdirs = glob.glob('%s/1[0-9][0-9][0-9][0-9]'%(path))
subdirs = glob.glob('%s/18301'%(path)) 


for dir in subdirs:
    print dir
    # Only run the following if your orientation was mixed up
    # BUT directional labels must be accurate in fslview
    # Make sure you verify that it worked
    #os.system("fslreorient2std  %s/anatomy/highres001  %s/anatomy/highres001"%(dir,dir))
    # bet call edit to use the flags you found worked well on your data
    os.system("bet %s/anat/T1 %s/anat/T1_brain -f .2 -B -m"%(dir,dir))
 # -R -m
 
# If you want to try out freesurfer, here's the command line code that
# you can adapt to the loop via os.system.  Mostly, you'll need to put actual paths in.
 
# I think it needs unzipped files (double check this)
# gunzip path/to/anatomy/highres001.nii.gz
 
# This takes a while (~15 minutes?)
#recon-all -autorecon1 -i path/to/anatomy/highres001.nii -subjid autorecon   -sd /path/to/anatomy/
# This will actually create the skull stripped brain (you won't get a mask)
 
#mri_convert  /path/to/anatomy/autorecon/mri/brainmask.mgz  --reslice_like /path/to/anatomy/highres001.nii /path/to/anatomy/highres001_brain.nii
 
# I'm deleting the files it created
#rm -rf /path/to/anatomy/autorecon/
 
# zipping up the skull stripped image and original image
#gzip /path/to/anatomy/*.nii
