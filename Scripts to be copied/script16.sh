#!/bin/bash

# Clear system logs
echo "Clearing system logs..."

# Clear log files
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/auth.log
sudo truncate -s 0 /var/log/kern.log
sudo truncate -s 0 /var/log/daemon.log
sudo truncate -s 0 /var/log/messages

# Clear journal logs (if using systemd)
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s

echo "System logs cleared."
