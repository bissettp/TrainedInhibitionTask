for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "circle 50,50 50, 1" $color.gif
done
