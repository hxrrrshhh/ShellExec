#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Error: Two numbers are required."
    exit 1
fi

# Assign the arguments to variables
num1=$1
num2=$2

# Calculate the modulus
modulus=$((num1 % num2))

# Display the result
echo "The remainder when $num1 is divided by $num2 is $modulus"

