#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Error: Two numbers are required."
    exit 1
fi

# Assign the arguments to variables
num1=$1
num2=$2

# Check for division by zero
if [ "$num2" -eq 0 ]; then
    echo "Error: Division by zero is not allowed."
    exit 1
fi

# Divide the numbers
quotient=$((num1 / num2))

# Display the result
echo "The quotient of $num1 divided by $num2 is $quotient"

