#!/bin/bash

# Automatically list disk partitions and their usage
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,ROTA

