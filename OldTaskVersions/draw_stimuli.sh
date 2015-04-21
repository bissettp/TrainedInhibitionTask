for color in red blue black
do
       convert -size 100x60 xc:skyblue -fill $color -stroke black -draw "circle 30,30 40,10" $color.gif
done
