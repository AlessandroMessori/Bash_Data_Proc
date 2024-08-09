echo "insert triangle sides:"

read l1
read l2
read l3

cathetis=$((l1 * l1 + l2 * l2))
ipho=$((l3 * l3))

if [ $cathetis -lt $ipho -o $cathetis -gt $ipho ]; then
	echo "False"
else
	echo "True"
fi
