# TeenConnect

Please install pcakages in REQUIREMENTS.txt

For Google calendar, we need to following the guidance to create service account:
https://developers.google.com/identity/protocols/oauth2/service-account

Create a local environment file .env, put the CAL_ID from Google service account in it.
Find the file teensconnect-website.json.TEMPLATE in home dir, fill the following information when you created google service account (or you can download the file directly after you created the service account from Google GUI):
    <keyid>
    <priviate_key>
    <client_email>
    <client_id>

Also, create a .gitignore file to stop github to upload this .env and teensconnect-website.json file. Example of the CLD_ID is:
CAL_ID=<id>@group.calendar.google.com
