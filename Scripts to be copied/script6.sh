#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Error: Two numbers are required."
    exit 1
fi

# Assign the arguments to variables
base=$1
exponent=$2

# Calculate the exponentiation using bc
result=$(echo "$base ^ $exponent" | bc)

# Display the result
echo "$base raised to the power of $exponent is $result"

