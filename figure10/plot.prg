#!/usr/bin/gnuplot

set terminal pngcairo enhanced
set output "syntheticdistrib.png"

set xlabel "adf rank"
set ylabel "adf (O^{2+})"

set xrange [0:155]
set log y

set style fill transparent solid 0.7
set boxwidth 1.0
set key inside top left

plot 'actual_pne' using 0:1 w boxes title "Observed", "<sort -g synthetic_pne" using 0:1 w boxes title "Modelled"
