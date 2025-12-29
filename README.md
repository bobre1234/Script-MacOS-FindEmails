# MacOS - FindEmails

This is a group of scripts which was used to retrieve emails from the Mail application on MacOS, the email tree structure is preserved. You must execute the script on the MacOS where you want to retrieve the emails. 

Stack : shell, python

## List and description of the scripts

**script1-findMail.sh**

> Find all emails in the MacOS and store all email's path in a text file "mailPathList.txt" in the current directory.

## Step to use all of the scripts

1. "script1-*" : copy all of the emails in a new directory to preserve the originals.
2. "script2-*" : create a text file with all email paths.
3. "script3-*" : create a directory "mailTree" with all sub-directories by the previous text file.
4. "script4-*" : move all of the copied mails by the script1 to the directories created by the script3.
