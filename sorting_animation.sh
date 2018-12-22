#!/bin/bash
declare -a sort=("5 2 4 3 1" " 52 4 3 1" " 25 4 3 1" "2  54 3 1" "2  45 3 1" "2 4  53 1" "2 4  35 1"
                 "2 4 3  51" "2 4 3  15" "2 4 3 1 5" "2 43  1 5" "2 34  1 5" "23  4 1 5" "23  4 1 5"
                 "2 3 4 1 5" "2 3 41  5" "2 3 14  5" "2 31  4 5" "2 13  4 5" "21  3 4 5" "12  3 4 5" "1 2 3 4 5")
declare -a unsort=("4 3 2 1 5" "1 5 4 3 2" "3 2 5 4 1" "2 3 5 1 4" "3 1 5 4 2" "5 2 4 3 1")
stty -echo # Disable input
tput civis # Hide the cursor
printf "Sorting  ${sort[0]}"
while true; do
  sleep 0.5
  for i in "${sort[@]}"; do
    printf "\rSorting  $i"
    sleep 0.05
  done
  sleep 0.5
  for i in "${unsort[@]}"; do
    printf "\rSorting  $i"
    sleep 0.02
  done
done
