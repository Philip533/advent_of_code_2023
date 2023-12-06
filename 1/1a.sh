#!/bin/bash
# Regex for if there are two numbers
first=`grep -oP '(\d).*(\d)(?!.*\d)' input | awk '{print substr($0, 1, 1), substr($0, length($0), 1)}'  | paste -d "" | sed 's/ //g' | awk '{s+=$0} END {print s}'`
# Catch if there is only 1 number and concatenate it with itself
last=`grep -oP '^[^0-9]*\d[^0-9]*$' input | grep -oP '\d'  | awk '{print $0, $0} ' | paste -d "" | sed 's/ //g' | awk '{k+=$0} END {print k}'`
echo $(($first+$last))
