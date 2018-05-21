from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import subprocess, time

timestamp = str(time.time()).split('.')[0]
subprocess.run(['fswebcam', '--no-banner', '~/RaspImages/{0}.jpg'.format(timestamp)])

gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")

if gauth.credentials is None: gauth.LocalWebserverAuth()
elif gauth.access_token_expired: gauth.Refresh()
else: gauth.Authorize()

gauth.SaveCredentialsFile("credentials.json")	
drive = GoogleDrive(gauth)

imageFile = drive.CreateFile({'title': '{}.jpg'.format(timestamp), 
	'parents': [{'kind': 'drive#fileLink', 'id': '1mBtabQjBNBfG4ZLldfPqjKh7iL9-ezTo'}]})
	
imageFile.SetContentFile('~/RaspImages/{0}.jpg'.format(timestamp))
imageFile.Upload()

