#!/bin/bash

# Set the username to 'hxrrrshhh'
USERNAME="hxrrrshhh"

# Check if the user exists
if id "$USERNAME" &>/dev/null; then
    echo "User Information for $USERNAME:"
    
    # Display user info
    echo "Username: $USERNAME"
    echo "User ID (UID): $(id -u $USERNAME)"
    echo "Group ID (GID): $(id -g $USERNAME)"
    echo "Groups: $(id -Gn $USERNAME)"
    echo "Home Directory: $(getent passwd $USERNAME | cut -d: -f6)"
    echo "Shell: $(getent passwd $USERNAME | cut -d: -f7)"
else
    echo "User $USERNAME does not exist."
    exit 2
fi

