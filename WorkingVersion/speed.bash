for ((j=0; j<=10; j++)); do
    for ((i=1; i<=16; i++)); do
        export  OMP_NUM_THREADS=$i
        time=$( TIMEFORMAT="%R"; { time ./main; } 2>&1 | sed -e 's/\,/./g')
        echo $time >> time$j.dat
    done
    echo "File $j done!"
done
