Provisioning the Server:
1. SSH into the server. The server will need to be running Ubuntu 16.04, as this is currently the only supported operating system for FBCTF.
2. Transfer the provision.sh script to any directory on the server.
   a. You must make this file executable. Run ‘chmod +x provision.sh’.
1. Run the provisioning script by typing ‘./provision.sh’. This script will automatically download the FBCTF platform and any dependencies for the question import script.
2. Once the script is finished running, navigate to the IP address of the server in your web browser. You should now have a fresh installation of FBCTF.
   a. Important Note: The admin password is printed to the console. Ensure you copy the password so you are able to login to the platform.


Importing the Questions:
1. SSH into the server running FBCTF. You must have already run the provisioning script.
2. Transfer the following files: import_questions.sh, country_iso.csv, insert_questions.py, questions.csv
   a. Type ‘chmod +x import_questions.sh’ to make the file executable.
   b. Do not run the python file directly. This is will not update the game cache, and the game board will not update.
1. Run the import_questions.sh script. This will take all of the questions and data from the questions.csv file. The script will match the country name in the questions.csv file to the country name in the country_iso.csv. If this file is not present in the same directory, the script will not run. 
2. Ensure that the script is completed without errors. If there was an error, the script will tell you which question it had an error with. You will have to manually fix the problem with that question. If there is no error, the script completed successfully.


Creating Bases (AWS Required):
1. Setup your workstation by installing the AWS command line interface. Then, ensure the python module ‘boto3’ is installed.
2. Launch the AWS EC2 instances with SSM enabled. Be sure your IAM user has all SSM privileges. 
3. Run the ssm_script.py file. This will ask for a comma separated list of IP addresses. Enter in all of the IP addresses that need to become bases.
4. In your browser, go to ip:12345 to ensure the base is running on each server.

If you want our entire configuration, you can use the admin panel and upload the attached SQL file. This includes the questions, teams, bases, categories, server settings.