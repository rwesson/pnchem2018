#!/bin/bash

rm -f list_30mar_classifications

while read p; do
  c=`/bin/grep ${p:0:10} weidmann.dat`
  echo $p $c >> list_30mar_classifications
done <list_30mar

more list_30mar_classifications | /bin/grep "W\|wels" | awk ' { print $4 } ' > adfs_hdef
more list_30mar_classifications | /bin/grep "W\|wels" | awk ' { print log($4)/log(10) } ' > adfs_hdef_log
more list_30mar | awk ' { print $NF } ' | sort -g > adfs_all
more adfs_all | awk ' { print log($1)/log(10) } ' > adfs_all_log
more list_30mar_classifications | /bin/grep -v "W" | awk ' { print $4 } ' > adfs_nohdef
more list_30mar_classifications | /bin/grep -v "W" | awk ' { print log($4)/log(10) } ' > adfs_nohdef_log
more list_30mar_b | awk ' { print $4 } ' > adfs_b
more list_30mar_b | awk ' { print log($4)/log(10) } ' > adfs_b_log
more list_30mar_nob | awk ' { print $4 } ' > adfs_nob
more list_30mar_nob | awk ' { print log($4)/log(10) } ' > adfs_nob_log
more list_30mar_classifications | /bin/grep "W" | awk ' { print $4 } ' > adfs_hdef_nowels
more list_30mar_classifications | /bin/grep "W" | awk ' { print log($4)/log(10) } ' > adfs_hdef_nowels_log

more adf-PNe-table-1.csv | grep HII | awk --field-separator="\t" ' { print $2 } ' | grep -v "5-8" > adfs_hii
more adf-PNe-table-2.csv | grep "PN\|new" | awk --field-separator="\t" ' { print $2 } ' | grep -v "5-8" > adfs_pne
