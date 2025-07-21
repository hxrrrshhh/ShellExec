#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Error: Two numbers are required."
    exit 1
fi

# Assign the arguments to variables
num1=$1
num2=$2

# Multiply the numbers
product=$((num1 * num2))

# Display the result
echo "The product of $num1 and $num2 is $product"

