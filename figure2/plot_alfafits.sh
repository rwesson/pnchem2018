#!/bin/bash

more /usr/share/alfa/optical_deep.cat | awk ' $1>4615 && $1<4680 { print $0 } ' > lineids.dat

# plotting details

echo "set terminal pngcairo enhanced size 960,1440" > plot.prg
echo "set output \"alfafits.png\"" >> plot.prg
echo "set multiplot layout 7,1" >> plot.prg

echo "set xrange [4610:4680]" >> plot.prg
echo "set yrange [-0.3:3]" >> plot.prg
echo "set ylabel \"Flux (H{/Symbol b}=100)\"" >> plot.prg

# normalise to Hb=100, offset to plot at rest wavelength, scale to max in range

for object in Fg1 Hen2-283 Hf2-2 MPA1759 NGC6326 NGC6337 Pe1-9
do

  hb=`grep flux /home/rwesson/data/objects/pnchem/python/${object}Blue_clean_1d.txt_lines.tex | awk ' { print $NF/100 } '`
  offset=`grep 4649.13 /home/rwesson/data/objects/pnchem/python/${object}Blue_clean_1d.txt_lines.tex | awk ' { print $1-$3 } '`
  max=`more /home/rwesson/data/objects/pnchem/python/${object}Blue_clean_1d.txt_lines.tex | awk -v hb=$hb ' BEGIN { max=0 } $1>4610 && $1<4680 && $5>max { max=$5 } END { print int(max)+1 } '`

  echo "set yrange [(-$max*0.1):$max]" >> plot.prg

# OII lines
  more lineids.dat | awk -v max=$max ' $3=="O" { print "set arrow "NR" from "$1","(-max/10)" to "$1","max" nohead dt 2" } ' >> plot.prg
# N lines
  more lineids.dat | awk -v max=$max ' $3=="N" { print "set arrow "NR" from "$1","(-max/10)" to "$1","max" nohead dt 3" } ' >> plot.prg
# C lines
  more lineids.dat | awk -v max=$max ' $3=="C" { print "set arrow "NR" from "$1","(-max/10)" to "$1","max" nohead dt 4" } ' >> plot.prg

  if [ "$object" == "Pe1-9" ]; then
    echo "set xlabel \"Wavelength (A)\"" >> plot.prg
  fi

  echo "plot '~/data/objects/pnchem/python/${object}Blue_clean_1d.txt_fit' using (\$1-$offset):(\$4/$hb) w l lc rgb 'black' title '$object', '' using (\$1-$offset):((\$3-\$5)/$hb) w l lw 2 lc rgb 'blue' dt 2 title 'fit', '' using (\$1-$offset):((\$3-\$2)/$hb) w l lc rgb 'red' dt 4 title 'residuals'" >> plot.prg

done

# and now plot

gnuplot plot.prg #&& rm plot.prg
