# TeenConnect

Please install pcakages in REQUIREMENTS.txt

For Google calendar, we need to following the guidance to create service account:
https://developers.google.com/identity/protocols/oauth2/service-account

Create a local environment file .env, put the CAL_ID from Google service account in it.

Also, create a .gitignore file to stop github to upload this .env file. Exaple of the CLD_ID is:
CAL_ID=<id>@group.calendar.google.com
