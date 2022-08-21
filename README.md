# TeenConnect

Please install pcakages in REQUIREMENTS.txt

For Google calendar, we need to following the guidance to create service account:
https://developers.google.com/identity/protocols/oauth2/service-account

Create a local environment file .env, put the CAL_ID from Google service account in it. Example of the CLD_ID is:
    CAL_ID=<id>@group.calendar.google.com

Find the file teensconnect-website.json.TEMPLATE in home dir, copy it to new file .teensconnect-website.json, note that there is a dot(.) before the file name. Then fill the following information to the file from created google service account (or you can download the file directly after you created the service account from Google GUI):
    <keyid>
    <priviate_key>
    <client_email>
    <client_id>

Also, The .gitignore file has been created for you to stop github to upload this .env and .teensconnect-website.json file. 

