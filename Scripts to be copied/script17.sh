#!/bin/bash

# Rotate logs manually using logrotate
echo "Manually rotating logs..."

# Force logrotate (all log files)
sudo logrotate -f /etc/logrotate.conf

# Manually rotate systemd journal logs
sudo journalctl --rotate

# Optionally, vacuum logs older than a specific period
sudo journalctl --vacuum-time=1d

echo "Logs rotated successfully."

