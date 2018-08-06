# the data: object, adf, period
echo "Abell 46	120	0.472" > data.tmp
echo "Ou 5    	56	0.364" >> data.tmp
echo "NGC 6778	18	0.15" >> data.tmp
echo "Hen 2-161	11	1.0" >> data.tmp
echo "Abell 63	8	0.456" >> data.tmp
echo "Hen 2-155	6.3	0.148" >> data.tmp
echo "IC 4776 	1.75	9" >> data.tmp
echo "NGC 5189	1.6	4.04" >> data.tmp
echo "Necklace	2.0	1.16" >> data.tmp
# new objects:
echo "Hf 2-2  	83	0.399	15	new" >> data.tmp
echo "Fg 1    	46	1.195	10	new" >> data.tmp
echo "Hen 2-283	5.1	1.128	0.5	new" >> data.tmp
echo "MPA1759 	62	0.503	8	new" >> data.tmp
echo "NGC 6326	23	0.37	3	new" >> data.tmp
echo "NGC 6337	18	0.173	2	new" >> data.tmp
echo "Pe 1-9  	60	0.140	10	new" >> data.tmp

# plot

echo 'set terminal png' > plot.prg
echo 'set xlabel "Binary period (days)"' >> plot.prg
echo 'set ylabel "adf(O^{2+})"' >> plot.prg
echo 'set output "adf-period.png"' >> plot.prg
echo 'set log x' >> plot.prg
echo 'set yrange [0:130]' >> plot.prg

echo 'set datafile separator "\t"' >> plot.prg
echo 'set arrow from 1.15,0.001 to 1.15,130 nohead' >> plot.prg
echo 'set label "adf=5.0" at 6.0,7.0' >> plot.prg
echo 'set label "period=1.15 days" at 1.35,60 rotate left' >> plot.prg
echo 'plot "data.tmp" using 3:2 notitle pt 7 ps 2,"<grep new data.tmp" using 3:2:4 w err notitle lc rgb "red" pt 5 ps 2,5.0 notitle#, "data.tmp" using 3:2:1 w labels notitle' >> plot.prg

gnuplot plot.prg && rm plot.prg

# make latex table

sort -t $'\t' -k 2 -g data.tmp | awk --field-separator="\t" ' { print $1" & "$2" & "$3" \\\\" } ' > table.tex

rm data.tmp
