SERVER DEPLYMENT REPORT 

#Author 
Anish Dhakal

#Date
07/01/2026

#Description 
This python project is based on a cloud-style server deployment report.
It reads server name from " servers.txt" which we assign ourself, assignes a 
random deploymet status [ Deployed , Pending, Failed ] and generates a formatted 
report with timestamps inside " deployment_report.txt".

This script use 'BASE_DIR'  to handle file path. so that it works on any machine 
without modification.


## Features
- Reads server names from a file
- Assigns random deployment status
- Generates a timestamped deployment report
- Professional formatting with columns
- Portable: works on any machine without editing paths

  ## How to Run
1. Clone the repository:
2. git clone https://github.com/anishdhakal/server-deployment-report.git
3. cd server-deployment-report
4. python deployment_report.py

#########################################################################

Folder Structure 
server-deployment-report/
|
── deployment_report.py       # Main script
── servers.txt                # Input file
── .gitignore                 # Ignore generated and unnecessary files
── README.md                  # Project documentation

Notes

* Deployment_report.txt is generated dynamically every time you run the script.
* The .gitignore ensures only source code and input files are tracked in Git.
* This project demonstrates Python file handling, random module usage,
and timestamp formatting in a cloud-style project context.
