Prerequisites
This is an example of how to list things you need to use the software and how to install them.

Python 3 - Download 
Pip 3 (usually gets installed automatically with Python)
MySQL Server - Download the package download, then create a user account and note the username and password
If all the above are satisfied, you may proceed to the next section.

Installation
Follow these insturctions to setup your own instance of the app:


1: Clone the repo
Find instructions for cloning/downloading this repo here, then unzip the repository

Or if you have git command line installed, clone using this command:

git clone https://github.com/Jain-Joseph1996/PythonProject

2: Cd to the folder
Open terminal/cmd/powershell and change directory/folder to the cloned folder. Here are the instructions

The command for the same would be

3: Install the PIP packages/dependencies
After you cd into the repo folder, ensure you see the following cmd/terminal prompt

pip install -r requirements.txt

4: Setup the database
To create the database from the MySQL schema:
Copy-paste the contents of sql/projectsql.sql directly into the MySQL command line, or


5: Add database credentials to the app
Start by renaming the .example.env file just .env, and then replacing the Your-Username and Your-Password values with the MySQL credentials.

6: Installing Fonts
In order to make the app's gui look good, you will have to install the Montserrat font. From the assets folder, install all three fonts (with .ttf format) by double clicking them.

7: It's done  | Run the app
Run main.py file with python 3 and you should see the login window, if you have followed each step correctly.

The default username and password are username and password respectively.



