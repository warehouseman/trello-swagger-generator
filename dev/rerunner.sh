#!/bin/sh
# export the_file="processValidValues.py"
# export the_file="processDefaults.py"
# export the_file="processArgument.py"
export the_file="processArguments.py"

while true; do
  change=$(inotifywait -e close_write .)
  change=${change#./ * }
  if [ "$change" = ${the_file} ]; then ./${the_file}; fi
done
