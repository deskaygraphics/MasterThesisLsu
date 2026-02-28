set terminal pngcairo size 900,520 enhanced font 'Arial,14'
set output 'media/vif_lollipop.png'

unset title
set xlabel "{/:Bold VIF}" font 'Arial-Bold,14'
set ylabel "" font 'Arial-Bold,14'

set xrange [0.0:3.5]
set yrange [0.5:12.5]

set border 3
set tics nomirror
unset grid
set key off

set ytics ( \
    "{/:Bold Geology}"          1, \
    "{/:Bold Well Influence}"   2, \
    "{/:Bold Dist. Fault}"      3, \
    "{/:Bold Curvature}"        4, \
    "{/:Bold LULC}"             5, \
    "{/:Bold TWI}"              6, \
    "{/:Bold TPI}"              7, \
    "{/:Bold Dist. River}"      8, \
    "{/:Bold Slope}"            9, \
    "{/:Bold Aspect}"          10, \
    "{/:Bold Precip.}"         11, \
    "{/:Bold Elevation}"       12  \
) font 'Arial,14'

set xtics 0.5 font 'Arial-Bold,14'

# Thin horizontal lines from 0 to each dot
set style arrow 1 nohead lw 1.5 lc rgb "#bbbbbb"
set arrow from 0,1  to 1.10,1  as 1
set arrow from 0,2  to 1.12,2  as 1
set arrow from 0,3  to 1.15,3  as 1
set arrow from 0,4  to 1.23,4  as 1
set arrow from 0,5  to 1.23,5  as 1
set arrow from 0,6  to 1.32,6  as 1
set arrow from 0,7  to 1.45,7  as 1
set arrow from 0,8  to 1.65,8  as 1
set arrow from 0,9  to 2.20,9  as 1
set arrow from 0,10 to 2.23,10 as 1
set arrow from 0,11 to 2.26,11 as 1
set arrow from 0,12 to 2.94,12 as 1

# Value labels
set label "{/:Bold 1.10}" at 1.10+0.07,1  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.12}" at 1.12+0.07,2  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.15}" at 1.15+0.07,3  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.23}" at 1.23+0.07,4  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.23}" at 1.23+0.07,5  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.32}" at 1.32+0.07,6  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.45}" at 1.45+0.07,7  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 1.65}" at 1.65+0.07,8  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 2.20}" at 2.20+0.07,9  font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 2.23}" at 2.23+0.07,10 font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 2.26}" at 2.26+0.07,11 font 'Arial,13' tc rgb "#333333"
set label "{/:Bold 2.94}" at 2.94+0.07,12 font 'Arial,13' tc rgb "#333333"

# Plot each point with a different color
plot \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#1f77b4" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#ff7f0e" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#2ca02c" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#d62728" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#9467bd" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#8c564b" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#e377c2" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#7f7f7f" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#bcbd22" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#17becf" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#aec7e8" notitle, \
  '-' using 2:1 with points pt 7 ps 2.2 lc rgb "#ffbb78" notitle
1  1.10
e
2  1.12
e
3  1.15
e
4  1.23
e
5  1.23
e
6  1.32
e
7  1.45
e
8  1.65
e
9  2.20
e
10  2.23
e
11  2.26
e
12  2.94
e
