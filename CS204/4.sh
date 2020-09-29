echo enter a number
read a

p=0
c=1

for (( i=0; i<a; i++))
do
    echo -n "$p "
    fn=$((p+c))
    p=$c
    c=$fn
done
