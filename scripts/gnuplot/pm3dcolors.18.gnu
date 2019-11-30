# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
set terminal  pngcairo truecolor enhanced  font "arial, 30" size 1920, 1680
set output 'pm3dcolors.18.png'
#set format cb "%3.1f" 
unset key
set style increment default
set view map scale 1
set samples 101, 101
set isosamples 2, 2
set style data pm3d
set style function pm3d
set xtics  norangelimit 2
unset ytics
unset ztics
set cbtics  norangelimit 0.1
set title "set palette rgbformulae 7,5,15" 
set xrange [ -10.0000 : 10.0000 ] noreverse nowriteback
set x2range [ * : * ] noreverse writeback
set yrange [ 0.00000 : 1.00000 ] noreverse writeback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ 0.00000 : 1.00000 ] noreverse nowriteback
set rrange [ * : * ] noreverse writeback
set pm3d explicit at b
g(x)=x
f(x)=(x+10)/20
## Last datafile plotted: "-"
splot f(x)
