for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "circle 50,50 50, 0" circle$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "rectangle 100,100 0, 0" square$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "rectangle 45,0, 55, 100" line$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "polygon 0, 0, 50, 100, 100, 0" invertedtriangle$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "polygon 0, 100, 50, 0, 100, 100" triangle$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "polygon 75, 7, 25, 7, 0, 50, 25, 93, 75, 93, 100, 50" hexagon$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "polygon 0, 50, 50, 0, 100, 50, 50, 100" diamond$color.gif
done

for color in white green blue yellow cyan magenta orange gray
do
       convert -size 101x101 xc:black -fill $color -stroke black -draw "path 'M 45,0 L 45,45 0,45 0,55 45,55 45,100 55,100 55,55 100,55 100,45 55,45 55,0 45, 0'" cross$color.gif
done