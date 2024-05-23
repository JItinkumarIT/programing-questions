import requests
from datetime import datetime
import base64

# Replace these variables with your actual values
organization = 'myorg'
project = 'myproject'
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
        
        # Print the pipeline details to inspect their structure
        print(f"Retrieved {len(pipelines)} pipelines")
        for pipeline in pipelines:
            created_date = datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').date()
            print(f"Pipeline ID: {pipeline['id']}, Name: {pipeline['name']}, Created Date: {created_date}")

        # Get the current month and year
        current_month = datetime.now().month
        current_year = datetime.now().year

        # Filter pipelines created in the current month
        new_pipelines = []
        for pipeline in pipelines:
            created_date = datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').date()
            if created_date.month == current_month and created_date.year == current_year:
                new_pipelines.append(pipeline)

        # Print the filtered pipelines
        print("\nPipelines created in the current month:")
        for pipeline in new_pipelines:
            created_date = datetime.strptime(pipeline['createdDate'], '%Y-%m-%dT%H:%M:%SZ').date()
            print(f"New Pipeline ID: {pipeline['id']}, Name: {pipeline['name']}, Created Date: {created_date}")

    except KeyError as e:
        print(f"Error: Missing key {e}")
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response")
        print(f"Response content: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
