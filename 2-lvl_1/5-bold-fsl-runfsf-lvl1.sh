#!/bin/bash
# Execute script via
# bash bold-fsl-runfsf-lvl1.sh

# This script runs the fsf file of everyone, but assumes it's been created already
#

## Run in parallel?
#export FSLPARALLEL=condor

## Set Base directory
basedir=/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses

## List subjects
#subs="17271 17276 17304 17315 17332"
#subs="17272 17273 17274 17275"
#subs="17277 17280 17288 17299"
#subs="17305 17312 17313 17314"
#subs="17316 17317 17318 17319"
#subs="17333 18009"
#subs="18072 18294"
#subs="18295 18300"
subs="18301 18305 18318 18319"

#17275 run 6


## list of runs 
runs="1 2 3 4 5 6"


## List model name/type
#model=fsfB

## Set type of fsf approach (trialwise, or basic)
type=lvl1_B
#block=regulate

## Remove earlier feat directory?
removefeat="true"

# Loop through every scan collected so far
for sub in $subs; do
	echo $sub
	for run in $runs; do
		echo $run
		#if [ "$removefeat" == "true" ]
			#then
				#rm -r ${basedir}/$sub/model/model001/${block}-run${run}.feat
	#	fi
		#CD to design dir and run fsf
		designDir=${basedir}/group/${type}_hab_feats_v1
		cd $designDir
		fsf=${type}TEMP${sub}-run${run}.fsf
		feat $fsf
		# Remove temp fsf file
		#rm ${fsf}
	done
done
