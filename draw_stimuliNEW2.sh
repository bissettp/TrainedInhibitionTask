for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "circle 50,50 50, 0" circle$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "rectangle 99,99 0, 0" square$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "rectangle 45,0, 55, 100" line$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "polygon 0, 0, 50, 100, 100, 0" invertedtriangle$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 100x100 xc:white -fill $color -stroke black -draw "polygon 0, 100, 50, 0, 100, 100" triangle$color.gif
done