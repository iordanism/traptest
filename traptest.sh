#!/bin/bash

echo "parallel working"
echo "hello trap"
if date -r 30
then
   echo "I've successfully printed out the date!"
else
   ls -l
fi
