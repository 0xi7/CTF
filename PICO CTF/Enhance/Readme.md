## To get the flag

```bash
cat drawing.flag.svg | grep -E "</tspan><tspan|</tspan></text>" | cut -d ">" -f 2 | cut -d "<" -f 1 | tr '\n' ' ' | tr -d ' '
```
