#!/usr/bin/env python
""" 
This script is used to create timing files from various conditions
I will produce 2 different timing files at this point
1) 3 column format by condition by run
2) 3 column format by trial by condition by run

"""
"""
Notes to self...Different experiment types
#train
expname = 'FCI_train' #e.g. Localizer phase or Training phase or conditioning
runs = np.array([1,2,3,4,5,6])
condnums = np.array([1,2])#num of conditions
condlabel = ('CSp', 'CSm')

#prelearning
expname = 'FCI_precond' #e.g. Localizer phase or Training phase or conditioning
runs = np.array([1,2,3])
condnums = np.array([1,2,3,4,5])
condlabel = ('CSpS', 'CSpNoS', 'CSpI', 'CSm', 'CSmI')

#learning
expname = 'FCI_cond' #e.g. Localizer phase or Training phase or conditioning
runs = np.array([1,2,3,4,5,6])
condnums = np.array([1,2,3,4,5])
condlabel = ('CSpS', 'CSpNoS', 'CSpI', 'CSm', 'CSmI', 'shock')

#regulate
expname = 'FCI_reg' #e.g. Localizer phase or Training phase or conditioning
runs = np.array([1,2,3,4,5,6,7,8])
condnums = np.array([1,2,3,4,5])
condlabel = ('CSpS', 'CSpNoS', 'CSpI', 'CSm', 'CSmI', 'shock')

"""


import numpy as np
import os
import pandas as pd #this is a cool dataframe python module

## Set directories

base_dir = '/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses'
os.chdir(base_dir)


# Set up details of experiment
expname = 'FCI_precond' #e.g. Localizer phase or Training phase or conditioning
sets = 'B'
task = 'Hab'
runs = np.array([1,2,3,4,5,6])
condnums = np.array([2,3,4,5])
condlabel = ('CSpNoS', 'CSpI', 'CSm', 'CSmI')


eventdur = 4
paramweight = 1

## Identify the model name(version)
model='model001'


#subs = ( '15207','15208','15209','15210','15211','15212','15213')

subs = ('17271', '17272', '17273', '17274', '17275', '17276', '17277', '17280', '17288', '17299', '17304', '17305', '17312', '17313', '17314', '17315', '17316', '17317', '17318', '17319', '17332', '17333', '18009', '18072', '18294', '18295', '18300', '18301', '18305', '18318', '18319')
#subs=('17280',)

for sub in subs:
	print sub
	os.chdir(base_dir + '/' + sub + '/bh/' + sub + '_' + sets + '_' + task)
	for run in runs:
		df_name = sub+ '-' +expname+ '-run' +str(run)+ '-log.txt'
		df = pd.read_csv(df_name)
		for i in np.arange(0,len(condnums)):
			## Create onsets directory if it doesn't exist
			onset_dir1 = base_dir+'/'+sub+'/model/'+model+'/onsets'+sets+task
			if not os.path.exists(onset_dir1):
				os.makedirs(onset_dir1)			
			## Create new dataframe of just the given condition
			#custom fix for shock event			
			df_cond = df[df.Condition==condnums[i]]
			numtrials = len(df[df.Condition==condnums[i]])
			## Create array in 3 column format for condition
			trialon = np.zeros([numtrials,3])
			trialon[:,0] = df_cond.GaborOn
			trialon[:,1] = eventdur
			trialon[:,2] = paramweight
			## Name file and save Whole condition timing file
			name = 	onset_dir1+'/'+expname+'-'+condlabel[i]+'-run'+str(run)+'.txt'
			np.savetxt(name, trialon, fmt='%3.3f', delimiter='\t')
			## Now iterate create trial wise onset files
			## Create onsets directory if it doesn't exist
			onset_dir2 = base_dir+'/'+sub+'/model/model002-trialglm/onsets'+sets+task
			if not os.path.exists(onset_dir2):
				os.makedirs(onset_dir2)
			for t in np.arange(0,numtrials):
				name = 	onset_dir2+'/'+expname+'-'+condlabel[i]+'-run'+str(run)+'-t'+str(t+1)+'.txt'
				trialont = np.zeros([1,3])
				trialont[0,:] = trialon[t,:]
				np.savetxt(name, trialont, fmt='%3.3f', delimiter='\t')


