#! /bin/sh - 

cat << "EOF"
 __  __             ___  ____
|  \/  | __ _  ___ / _ \/ ___|
| |\/| |/ _` |/ __| | | \___ \
| |  | | (_| | (__| |_| |___) |
|_|__|_|\__,_|\___|\___/|____/             _ _
|  ___(_)_ __   __| | ____|_ __ ___   __ _(_) |___
| |_  | | '_ \ / _` |  _| | '_ ` _ \ / _` | | / __|
|  _| | | | | | (_| | |___| | | | | | (_| | | \__ \
|_|   |_|_| |_|\__,_|_____|_| |_| |_|\__,_|_|_|___/

You must use this script on MacOS.
Your Terminal must have the complete access to the disk.
You must be root to use this script.

Version:12/2025
Author:bobre
_____________________________________________________

EOF

echo "Starting the script..."

#Check if the directory exists

if ls -d ~/Library/Mail/V* >/dev/null 2>&1; then
	echo "OK - The directory exists"
else
	echo "ERROR - the mail directory doesn't exists"
	exit 1
fi

#Find all email files in the specific MacOS directory
#Create text file with all path and copy emails in a new directory

echo "Searching emails..."

find ~/Library/Mail/V* -name "*.emlx" 2>/dev/null | grep -v "partial" > ./mailPathList.txt

nbLineOutput=$(wc -l < mailPathList.txt 2>/dev/null)
if [ $nbLineOutput -gt 0 ]; then
       echo "OK - Emails found and mailPathList.txt created in Document"
else
	echo "ERROR - No email found"		
	exit 1
fi

echo "Create allCopiedEmails directory"

mkdir ./allCopiedEmails

find ~/Library/Mail/V* -name "*.emlx" 2>/dev/null | grep -v "partial" | while read -r f; do cp "$f" ./allCopiedEmails/$(date +%s%N)_$(basename "$f"); done

echo "OK - The script is complete"
echo "OK - Please use the script2"		
exit 0
