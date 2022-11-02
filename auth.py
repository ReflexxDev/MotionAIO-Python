import re
import time
import uuid
from datetime import datetime
import requests
from pypresence import Presence


FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"
Reset = "\x1b[0m"



API_KEY = 'pk_aCNZOQmLLP42C8pNQCsRnsJEdc4UaNXw'

def log(content):
	print('[{}] {}'.format(datetime.utcnow(), content))
  
def get_license(license_key):
	headers = {
		'Authorization': f'Bearer {API_KEY}'
	}

	req = requests.get(f'https://api.metalabs.io/v4/licenses/{license_key}', headers=headers)
	if req.status_code == 200:
		return req.json()

	return None

def update_license(license_key, hardware_id):
	headers = {
		'Authorization': f'Bearer {API_KEY}',
		'Content-Type': 'application/json'
	}

	payload = {
		'metadata': {
			'hwid': hardware_id
		}
	}

	req = requests.patch(
		f'https://api.metalabs.io/v4/licenses/{license_key}',
		headers=headers,
		json=payload
	)

	if req.status_code == 200:
		return True

	return None

def check_license(license_key):
	license_data = get_license(license_key.strip())
	if license_data:
		name = license_data["user"]["username"]
		disc = license_data["user"]["discriminator"]
		hardware_id = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		if license_data.get('metadata', {}) == {}:
			updated = update_license(license_key, hardware_id)
			if updated:
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgGreen + "Sucesfully Authenticated -> " + name + " #" + disc + Reset)
			else:
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Something Went Wrong, Please Contact Support" + Reset)
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
				time.sleep(10)
				exit()
		else:
			current_hwid = license_data.get('metadata', {}).get('hwid', '')
			if current_hwid == hardware_id:
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgGreen + "Sucesfully Authenticated -> " + name + " #" + disc + Reset)
			else:
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Licence Already In Use On Another Machine!" + Reset)
				print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
				time.sleep(10)
				exit()
                
	else:
		print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Licence Not Found" + Reset)
		print("[" + str(datetime.now()) + "]" + " " + "|" + " " + FgRed + "Exiting In 10 Seconds" + Reset)
		time.sleep(10)
		exit()
        
        