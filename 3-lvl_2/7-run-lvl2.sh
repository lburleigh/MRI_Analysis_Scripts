#!/bin/bash
# Execute script via
# bash 7-run-lvl2.sh

# This script runs the fsf file of everyone, but assumes it's been created already
#

## Run in parallel?
#export FSLPARALLEL=condor

## Set Base directory
basedir=/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses

## List subjects
#subs="17271 17272 17273 17274 17275" 
#subs="17276 17277 17280 17288 17299" 
#subs="17304 17305 17312 17313 17314"
#subs="17315 17316 17317 17318 17319" 
#subs="17332 17333 18009 18072 18294"
#subs="18295 18300 18301 18305"
subs="18318 18319"


## list of runs
runs="1 2 3 4 5 6"
#runs="1 2 3"

## List model name/type
model=B

## Set type of fsf approach (trialwise, or basic)
type=B_hab
#block=regulate

## Remove earlier feat directory?
removefeat="true"

# Loop through every scan collected so far
for sub in $subs; do
	echo $sub
	#if [ "$removefeat" == "true" ]
		#then
		#rm -r ${basedir}/$sub/model/model001/${block}-run${run}.feat
	#fi
	#CD to design dir and run fsf
	designDir=${basedir}/group/lvl2_${type}_feats_v1
	cd $designDir
	fsf=${type}-lvl2fe-TEMP${sub}.fsf
	feat $fsf
	# Remove temp fsf file
	#rm ${fsf}
done
