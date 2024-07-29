#!/usr/bin/env python3

import os
import time

print("Check if the network is available")
print(" ")

def check_network():
    """Check if the network is available"""
    response = os.system("ping -c 1 google.com > /dev/null 2>&1")
    return response == 0

while True:
    print(" ")
    print(f"Network UP at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    if not check_network():
        print(f"Network down at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(3)
