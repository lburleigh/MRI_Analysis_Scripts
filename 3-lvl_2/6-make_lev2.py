#!/usr/bin/python

# This creates the level1 fsf's and the script to run the feats on condor

import os
import glob

studydir ='/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'

fsfdir="%s/group/lvl2_B_hab_feats_v1"%(studydir)

subdirs=glob.glob("%s/1[0-9][0-9][0-9][0-9]"%(studydir))
#subdirs=glob.glob("%s/18301"%(studydir))

setnum = 'B'


for dir in list(subdirs):
  splitdir = dir.split('/')
  splitdir_sub = splitdir[7]  # You will need to edit this
  subnum=splitdir_sub[-5:]    # You also may need to edit this
  subfeats=glob.glob("%s/model/B_hab_lvl1_v1/B_run[0-9].feat"%(dir))
  if len(subfeats)==6:  # Add your own second loop for 2 feat cases
    print(subnum)
    replacements = {'17271':subnum}
    with open("%s/lvl2_B.fsf"%(fsfdir)) as infile: 
      with open("%s/B_hab-lvl2fe-TEMP%s.fsf"%(fsfdir, subnum), 'w') as outfile:
          for line in infile:
            for src, target in replacements.iteritems():
              line = line.replace(src, target)
            outfile.write(line)
    
