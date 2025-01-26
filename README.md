# WhatBytes_Assignment
Django Assignment

Overview
Your task is to create a Django application with the following functionality:
User authentication with email or username and password.
Pages for login, signup, forgot password, change password, dashboard, and profile.
Restrict access to certain pages based on authentication status.

Requirements
1. Login Page
	Display two fields: Username/Email and Password.
	Include links/buttons for Sign Up and Forgot Password.
2. Sign Up Page
	Include fields for Username, Email, Password, and Confirm Password.
	Include a link/button to go back to the Login page.
3. Forgot Password Page
	Include a field for Email and a button to send reset instructions.
	Upon clicking the button, send an email with a link to reset the password.
4. Change Password Page
  Require authentication to access this page. 
  Include fields for Old Password, New Password, and Confirm Password.
  Include a link/button to go back to the Dashboard.
5. Dashboard
  Only accessible to authenticated users.
  Display a greeting message like "Hi, username!".
  Include links to the Profile page and Change Password page.
  Provide an option to logout.
6. Profile Page
  Display information such as Username, Email, Date Joined, and Last Updated.
  Include a link/button to go back to the Dashboard.
  Provide an option to logout.

Note: 
The project fulfills all the requiremnets.
One key feature is that once 'logout' is clicked on a page, then the cache of the browser is cleared so that the previous authenticated pages cannot be accessed.
No styling is provided for the web pages. 

Instructions to Run: 

1. Pull the repository.
2. Start the virtual enviournment using the following command : .venv/Scripts/activate
3. Change the directory to user_authentication: cd user_authentication
4. Run the local server : python manage.py runserver
