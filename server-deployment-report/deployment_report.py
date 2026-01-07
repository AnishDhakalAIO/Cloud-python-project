"""
Project 1: Server Deployment Report
Author: Anish Dhakal
Date: 2026-01-07

Description:
Reads server names from a file, assigns random deployment status,
and generates a formatted deployment report with timestamps.
"""

import random
from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

servers_path = os.path.join(BASE_DIR, "servers.txt")
report_path = os.path.join(BASE_DIR, "deployment_report.txt")


# Read server names
try:
    with open(servers_path, "r") as file:
        servers = [line.strip() for line in file]
except FileNotFoundError:
    print("Error: {servers_path} not found")
    exit()

statuses = ["DEPLOYED", "FAILED", "PENDING"]

# Generate deployment report
with open(report_path, "w") as report:
    report.write(f"{'SERVER-NAME':<12}{'STATUS':<10} {'TIMESTAMP'}\n")
    report.write("---------------------------------------\n")

    for server in servers:
        status = random.choice(statuses)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report.write(f"{server:<12}{status:<10} {timestamp}\n")

print("Deployment report generated successfully!")
