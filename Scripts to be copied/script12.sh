#!/bin/bash

# Check if the correct number of arguments are passed
if [ "$#" -ne 1 ]; then
    echo "Error: One argument (folder name) is required."
    echo "Usage: $0 <folder_name>"
    exit 1
fi

# Assign the argument to a variable
folder_name=$1

# Create the folder
mkdir -p "$folder_name"
echo "Folder '$folder_name' created."

