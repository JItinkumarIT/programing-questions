import requests
from datetime import datetime

# Replace these variables with your actual values
organization = 'your_organization'
project = 'your_project'
pat = 'your_personal_access_token'

# Basic authentication
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {pat}'
}

# API endpoint to list all pipelines
url = f'https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=6.0'

response = requests.get(url, headers=headers)
pipelines = response.json()['value']

# Get the current month and year
current_month = datetime.now().month
current_year = datetime.now().year

# Filter pipelines created in the current month
new_pipelines = [pipeline for pipeline in pipelines if datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').month == current_month and datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').year == current_year]

for pipeline in new_pipelines:
    print(f"Pipeline ID: {pipeline['id']}, Name: {pipeline['name']}, Created Date: {pipeline['createdDate']}")




import requests
from datetime import datetime
import base64

# Replace these variables with your actual values
organization = 'your_organization'
project = 'your_project'
pat = 'your_personal_access_token'

# Encode the PAT for Basic Auth
pat_encoded = base64.b64encode(f':{pat}'.encode()).decode()

# Basic authentication
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {pat_encoded}'
}

# API endpoint to list all pipelines
url = f'https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=6.0'

response = requests.get(url, headers=headers)

# Check response status
if response.status_code != 200:
    print(f"Failed to fetch pipelines: {response.status_code} {response.reason}")
    print(response.text)
else:
    try:
        pipelines = response.json()['value']
        # Get the current month and year
        current_month = datetime.now().month
        current_year = datetime.now().year

        # Filter pipelines created in the current month
        new_pipelines = [pipeline for pipeline in pipelines if datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').month == current_month and datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').year == current_year]

        for pipeline in new_pipelines:
            print(f"Pipeline ID: {pipeline['id']}, Name: {pipeline['name']}, Created Date: {pipeline['createdDate']}")
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response")
        print(f"Response content: {response.text}")
