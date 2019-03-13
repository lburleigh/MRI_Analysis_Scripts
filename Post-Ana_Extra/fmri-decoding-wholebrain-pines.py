#!/usr/bin/python

%matplotlib gtk
#%matplotlib inline #for use in jupyter
from nltools.data import Brain_Data
import matplotlib.pyplot as plt
from matplotlib import interactive
import os
import numpy as np
import pandas as pd
import seaborn as sns
import glob
from nltools.plotting import plotBrain
%pylab


# Find nii files and load
basedir = os.path.join('/mnt/scratch-800/FCI/group/decoding-whole')

# Saving info
phase='regulate'

# concatenate the brain data
fname = sorted(glob.glob(basedir+ '/152[0-9][0-9]-'+phase+'-cs*.nii.gz'))

# Create labeling vector Y and subject list, and load imaging data
data = Brain_Data()
Y = []
sublist = []
for f in fname:
	# extract condition and append to Y vector
    Y.append(f.split(phase+'-')[-1][0:4])
	# extract subject id and append to sublist
    sublist.append(f.split('/')[-1][0:5])
	# Load data using Brain_Data object of nltools
    data = data.append(Brain_Data(f))

# Plot dataset
#plotBrain(data.mean())

# Load neurosynth map for testing maps correlation with some thing
topicmap = Brain_Data(os.path.join(basedir,'Rating_Weights_LOSO_2.nii.gz'))
# Replace 0 with nan
#topicmap.data[topicmap.data==0]=np.nan
#plotBrain(topicmap)

# Predictions from whole brain
predicted_emotion = data.similarity(topicmap,'correlation')
predicted_emotion

# save to file
# Create group dictionary then data frame for Saving
grpdic={'sub':sublist,'condition':Y,'prediction':predicted_emotion}
df=pd.DataFrame(grpdic, columns=['sub','condition','prediction'])
filename=basedir+'/results_'+phase+'-pinesdecode.csv'
df.to_csv(filename,index=False)


# Plot results summary
dat = pd.DataFrame(data={'Predicted':predicted_emotion,'Condition':Y})
with sns.plotting_context(context='paper',font_scale=2):
    ax = sns.factorplot(data=dat,x='Condition',y='Predicted')
plt.title("Anxiety Predicting CS+ versus CS- PINES\n")

# Compare
a = dat.Predicted[dat.Condition=='csp.']
b = dat.Predicted[dat.Condition=='csm.']

import scipy.stats as stats
stats.ttest_rel(a,b)
