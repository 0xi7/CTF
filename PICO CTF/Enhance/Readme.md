## To get the flag

cat drawing.flag.svg | grep -E '</tspan><tspan|</tspan></text>' | cut -d '>' -f 2 | cut -d '<' -f 1 | tr -d '\n' | tr -d ' '
