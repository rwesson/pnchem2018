# get results
# for gnuplot, specify them as x,y,xlow,xhigh,ylow,yhigh

for object in Hf2-2 Hen2-283 NGC6326 NGC6337 MPA1759
do

  grep "He+" $object*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } NF>7 { print pmid,$7,$2,p2,$7+$9,$7+$8 } ' > ${object}_He+.dat
  grep "He2+" $object*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } NF>7 { print pmid,$7,$2,p2,$7+$9,$7+$8 } ' > ${object}_He2+.dat
  grep "He/H" $object*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } NF>7 { print pmid,$7,$2,p2,$7+$9,$7+$8 } ' > ${object}_He.dat

  grep "\[OIII\] temp" $object*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } { print pmid,$8,$2,p2,$8+$9,$8+$10 } ' > ${object}_te_oiii.dat
  grep "adf (O/" ${object}*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } { print pmid,$8,$2,p2,$8+$9,$8+$10 } ' > ${object}_adf_o.dat
  grep "O/H  " ${object}*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } NR%2==1 { print pmid,$7,$2,p2,$7+$8,$7+$9 } ' > ${object}_o_cels.dat
  grep "O/H  " ${object}*results | awk --field-separator="[_ ]+" ' { p2=substr($3,1,3); pmid=($2+p2)/2 } NR%2==0 { print pmid,$7,$2,p2,$7+$8,$7+$9 } ' > ${object}_o_rls.dat

# remove spuriously high O/H from CELs at central star pos in NGC 6337:

  if [ "$object" == "NGC6337" ]; then
    sed -i -e 's/^375.5/#375.5/g' NGC6337_o_cels.dat
  fi

  echo "set terminal pngcairo enhanced color" > plot.prg
  echo "set datafile missing '--'" >> plot.prg
  echo "set output \"${object}_He.png\"" >> plot.prg
  echo "plot '${object}_He.dat' w xyerr title 'He/H', '${object}_He+.dat' w xyerr title 'He^{+}/H^{+}', '${object}_He2+.dat' w xyerr title 'He^{2+}/H^{+}" >> plot.prg

  echo "set output \"${object}_O.png\"" >> plot.prg
  echo "plot '${object}_o_cels.dat' w xyerr title 'O/H (CELs)', '${object}_o_rls.dat' w xyerr title 'O/H (RLs)'" >> plot.prg

  echo "set output \"${object}_Te.png\"" >> plot.prg
  echo "plot '${object}_te_oiii.dat' w xyerr title 'T_{e} ([O III])'" >> plot.prg

  gnuplot plot.prg

done
