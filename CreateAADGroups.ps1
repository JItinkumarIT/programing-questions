# Function to check if a group exists in AAD
function Get-AADGroup {
    param (
        [string]$GroupName
    )

    $group = Get-AzureADGroup -Filter "DisplayName eq '$GroupName'"
    return $group
}

# Function to create a group in AAD
function Create-AADGroup {
    param (
        [string]$GroupName,
        [string]$Description
    )

    $group = New-AzureADGroup -DisplayName $GroupName -MailEnabled $false -SecurityEnabled $true -MailNickname $GroupName -Description $Description
    return $group
}

# Function to ensure a group exists
function Ensure-AADGroup {
    param (
        [string]$GroupName,
        [string]$Description
    )

    $group = Get-AADGroup -GroupName $GroupName
    if (-not $group) {
        Write-Output "Creating group: $GroupName"
        Create-AADGroup -GroupName $GroupName -Description $Description
    } else {
        Write-Output "Group already exists: $GroupName"
    }
}

# Main function to create groups for a project
function Create-ProjectGroups {
    param (
        [string]$ProjectName
    )

    $baseGroupName = "ADO-Project-$ProjectName"

    $roles = @(
        "Build Administrators",
        "Contributors",
        "Endpoint Administrators",
        "Endpoint Creators",
        "Project Administrators",
        "Project Valid Users",
        "Readers",
        "Release Administrators"
    )

    foreach ($role in $roles) {
        $groupName = "$baseGroupName-$role"
        Ensure-AADGroup -GroupName $groupName -Description "$role group for $ProjectName project"
    }
}

# Connect to Azure AD
Connect-AzureAD

# Example usage
param (
    [string]$ProjectName
)

if (-not $ProjectName) {
    Write-Error "Please provide a project name."
    exit 1
}

Create-ProjectGroups -ProjectName $ProjectName
