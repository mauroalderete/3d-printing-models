#!/bin/sh

# Skew ratio to fix the skew in the print
ratio=-0.0153

prusa_output=$SLIC3R_PP_OUTPUT_NAME
path=$(dirname $prusa_output)
name=$(basename $prusa_output)
skew_output=$path/${name%.*}_skewed.gcode

# Prepare temporal file
temporal_file=~/tmp/gcode-cli-$(date +%Y%m%d-%H%M%S).log
mkdir -p ~/tmp
touch $temporal_file

# Log post-processing

echo "Starting post-processing" >> $temporal_file

echo "Post-processing G-code file: $*" >> $temporal_file
echo "Prusa output: $prusa_output" >> $temporal_file
echo "Path: $path" >> $temporal_file
echo "Name: $name" >> $temporal_file
echo "Skew output: $skew_output" >> $temporal_file
echo "Ratio: $ratio" >> $temporal_file

echo "Prusa env variables:" >> $temporal_file
env | grep ^SLIC3R >> $temporal_file

echo "Starting skew process" >> $temporal_file

# Run skew process
~/.goenv/shims/gcode-cli skew xy --ratio $ratio --output $skew_output $prusa_output >> $temporal_file 2>&1

echo "Skew process finished" >> $temporal_file
echo "Skewed file: $skew_output" >> $temporal_file

echo "End of post-processing" >> $temporal_file
