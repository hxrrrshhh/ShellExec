#!/bin/bash

# This script will list all partitions on the system

echo "Listing all partitions on the system:"

# Use the 'lsblk' command to list all partitions
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT

