#!/bin/bash
#
# Launches multiple threads for execution. The ParselTongue start file has been
# edited to support the non-interactive nature of the application.

i=10
while [ $i -lt 13 ]
do
	start_parseltongue.sh THREAD$i/ $i ../$[$i-10]'exec'.py & 
	i=$[$i+1]
	sleep 10
done
