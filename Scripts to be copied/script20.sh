#!/bin/bash

# This script will show all open ports using ss (recommended over netstat)
# You can modify the command if you want to use netstat

echo "Showing all open ports on the system:"

# Use ss to display open ports
ss -tuln

