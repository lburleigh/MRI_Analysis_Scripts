#!/bin/bash
# Execute script via
# bash bold-fsl-lvl3-clusteratlasquery.sh

## Run Cluster on image, likely group level stats
## Then run Atlasquery on to determine were those clusters
## are anatomically

## OR just run autoaq to autmatically generate a cluster report and run atlas query

## Set base directory
basedir=/mnt/12TB-volume/Experiments/FCI/group/bold-CSp-CSmF12wOD.gfeat/cope1.feat
#basedir=/mnt/12TB-volume/Experiments/FCI/group/bold-CSpi-CSmiF12wOD.gfeat/cope1.feat


## Run FSL's cluster
cluster -i $basedir/thresh_zstat2 -t 2.3 --mm -o $basedir/clusti-CSm-CSpF12wOD > $basedir/cluster-info-CSm-CSpF12wOD.txt

## Run FSL's Atlasquery
#atlasquery -a "Harvard-Oxford Subcortical Structural Atlas" -m $basedir/clusti-CSp-CSmF12wOD > $basedir/atlasq-HOsubc-CSp-CSm.txt
#atlasquery -a "Harvard-Oxford Cortical Structural Atlas" -m $basedir/clusti-CSp-CSmF12wOD > $basedir/atlasq-HOcort-CSp-CSm.txt

## Run auto atlas query which can do cluster and atlasquery in one, but doesn't create a new mask
## the -u command can be used to append data to existing file without overwrite
autoaq -i $basedir/thresh_zstat1 -t 2.3 -o $basedir/clust-report-CSpi-CSmi.txt -a "Harvard-Oxford Subcortical Structural Atlas"
autoaq -i $basedir/thresh_zstat1 -t 2.3 -u -o $basedir/clust-report-CSpi-CSmi.txt -a "Harvard-Oxford Cortical Structural Atlas"
