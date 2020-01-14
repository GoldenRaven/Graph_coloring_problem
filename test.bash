#!/bin/bash
rm -f min_color_num-depth min_color_num-max_closed
echo "color num and node color is wirtten in file 'min_color_num-depth'"
echo "least color num is wirtten in file 'min_color_num-max_closed'"
echo "Be patient, it takes minutes."
for file in gc_*
do
    cp  $file input
    echo "testing $file in method1 ..."
    #test method one in file color_by_depth.py
    echo $file " :" >> min_color_num-depth
    python color_by_depth.py >> min_color_num-depth
    echo "" >> min_color_num-depth
    #find the least number of color with the method in file
    echo "testing $file in method2 ..."
    if [ $file == "gc_1000_5" ]
    then
        echo "data gc_1000_5 costs too much time in this method, skipping!"
        continue
    fi
    echo $file " :" >> min_color_num-max_closed
    python search_max_closed.py >> min_color_num-max_closed
    echo "" >> min_color_num-max_closed
done
