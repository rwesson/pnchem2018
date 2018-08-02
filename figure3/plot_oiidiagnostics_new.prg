#!/usr/bin/gnuplot

set terminal png enhanced size 960,720 font ",14"
set output "oii_diagnostics_new.png"

set label "log T_e (K)" at 2.5,4.2 textcolor rgb "red"
set label "log n_e (cm^{-3})" at 4.5,0.6 textcolor rgb "blue"

set mxtics 5
set mytics 5
set xrange [1.8:5.0]
set yrange [0.0:4.5]
set xlabel "OII 4649/4089"
set ylabel "OII 4649/4662"

set label "←Hen 2-283" at 1.85,2.4

plot '/home/rwesson/data/objects/pnchem/python/oiinew/ratios.dat' using 2:5:($2+$3):($2+$4):($5+$6):($5+$7) w xyerr notitle,\
'/home/rwesson/data/objects/pnchem/python/oiinew/ratios.dat' using 2:5 pt 7 lt 1 notitle,\
"<tail -n 11 /usr/share/neat/te_oii.dat | awk ' { print $1+0.15,$2,(NR*0.4)+0.8 } '" w labels textcolor rgb "blue" notitle,\
"<awk ' NR%10==3 && NR>4 { print $1,($2+0.15),((NR-3)*0.02)+2.4 } ' /usr/share/neat/te_oii.dat" w labels textcolor rgb "red" notitle,\
"<awk ' NR%10==0 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==1 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==2 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==3 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==6 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==7 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==8 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"<awk ' NR%10==9 { print $0 } ' /usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"/usr/share/neat/te_oii.dat" w l lt 2 notitle,\
"/home/rwesson/data/objects/pnchem/python/oiinew/ratios.dat" using 2:($5+0.05):1 w labels notitle
