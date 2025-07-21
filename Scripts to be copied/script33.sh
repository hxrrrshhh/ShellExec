#!/bin/bash

# Set the username to 'hxrrrshhh'
USERNAME="hxrrrshhh"

# Get the user group membership
USER_GROUPS=$(groups $USERNAME)

# Check if the user exists and display group membership
if [ $? -eq 0 ]; then
    echo "$USERNAME is a member of the following groups: $USER_GROUPS"
else
    echo "User $USERNAME does not exist."
    exit 2
fi

