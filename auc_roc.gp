set terminal pngcairo size 750,700 enhanced font 'Arial,14'
set output 'media/auc_roc_et_rf.png'

unset title
set xlabel "{/:Bold False Positive Rate}" font 'Arial-Bold,14'
set ylabel "{/:Bold True Positive Rate}" font 'Arial-Bold,14'

set xrange [0:1]
set yrange [0:1]
set xtics 0.2 font 'Arial-Bold,14'
set ytics 0.2 font 'Arial-Bold,14'

set border 3
set tics nomirror
set grid lt 1 lc rgb "#dddddd"
set key right bottom font 'Arial,12' box lc rgb "#999999"
set size ratio 1

# Diagonal reference line
set arrow from 0,0 to 1,1 nohead lc rgb "gray" lw 1.2 dt 2

# ET ROC: AUC = 0.9663
# RF ROC: AUC = 0.9448
# Data generated from sklearn roc_curve, exported below

plot 'media/roc_et.dat' using 1:2 with lines lw 2.5 lc rgb "#2166ac" title "Extra Trees (AUC = 0.9663)", \
     'media/roc_rf.dat' using 1:2 with lines lw 2.5 lc rgb "#b2182b" title "Random Forest (AUC = 0.9448)"
