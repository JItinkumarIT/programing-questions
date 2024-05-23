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
