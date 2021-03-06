#!/bin/bash

######################################################################################!/bin/bash

#####################################################################################
## SCRIPT TO COMBINE correlational maps from a beta-serires analysis for a 3rd level group analysis
##
## Refer to the README.doc for Maarten Mennes' step-by-step how-to
## Written by Lin Nga, USC 11/2010 for the ICBM resting state data
##
#####################################################################################

## set DIRectories
#outDir=`pwd`
outDir=/mnt/40TB-raid6/Experiments/FCTM_S/FCTM_S_Data/Analyses/group/lvl3_AvB
FinalOut=${outDir}/v1.gfeat
standard=/usr/share/data/fsl-mni152-templates/MNI152_T1_2mm_brain.nii.gz 

# Make the design files. Help can be found here: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/GLM/CreatingDesignMatricesByHand?fbclid=IwAR3QerRZzYomuKpqkRxIpZ6OEcQNae1OFYgOSilX8wdELdArF3AWSCBwuzA
designmat=${outDir}/design.mat
designcon=${outDir}/design.con
#designgrp=${outDir}/design.grp



if [ ! -e $FinalOut ]; then
	echo " ---- process start ---- "
	izmap=4d_lc_seed_maps.nii.gz # you need to create 4d image file by time-basis concatenating individual copes (or others) 
	nEV=`fslnvols ${izmap}`

	# mask 
	if [ ! -e mask.nii.gz ]; then
		echo "Mask Generation"
		fslsplit ${izmap} tmp
		for itmp in tmp*.nii.gz; do
			fslmaths ${itmp} -abs -bin ${itmp}
		done

		fslmerge -t mask.nii.gz `ls -f tmp*.nii.gz`
		fslmaths mask.nii.gz -Tmin mask.nii.gz
		rm -r tmp*.nii.gz
	fi	
          	    
	## 3. Run group analysis w/flameo in flame1 mode
	echo "Running flameo"
	FSLPARALLEL=10;export FSLPARALLEL
	flameo --cope=${izmap} --mask=mask.nii.gz --dm=${designmat} --tc=${designcon} --cs=${designgrp} --ld=${FinalOut} --runmode=flame12


	## 4. Use easythresh to do GRF correction
	echo "Thresholding and collecting results: $analysis"
	cd ${FinalOut}

	DLH=`smoothest -d $nEV -m mask -r res4d.nii.gz | grep DLH | awk '{print $2}'`
	Vol=`smoothest -d $nEV -m mask -r res4d.nii.gz | grep VOLUME | awk '{print $2}'`
	echo "DLH=$DLH vol=$Vol df=$nEV"

	for x in zstat*.nii.gz; do
		x=`echo $x | sed s@.nii.gz@@g`
		n=`echo $x | sed s@zstat@@g`

		easythresh ${x} ./mask.nii.gz 2.3 0.05 ${standard} ${x}		
		cluster -i thresh_zstat${n} -c cope${n} -t 2.3 -p 0.05 -d $DLH --volume=$Vol --othresh=thresh_zstat${n} -o cluster_mask_zstat${n} --connectivity=26 --mm --olmax=lmax_zstat${n}_std.txt > cluster_zstat${n}_std.txt

		fslstats thresh_zstat${n} -l 0.0001 -R >> thresholds.txt
		len=`cat lmax_${x}_std.txt | wc -l`
		GRPcontrast=`grep "/ContrastName${n}" ${designcon} | awk '{print $2}'`
		if [ $len -ne 1 ]; then
		   ((lenWOhdr=len-1))
		   i=0
		   while [ $i -lt $lenWOhdr ]; do
				((i++))
				line=`tail -n $lenWOhdr lmax_${x}_std.txt | sed -n "${i}"'p'`
				echo "$line $GRPcontrast" >> ${FinalOut}/lmax.txt
		   done
		fi		
	done
fi
