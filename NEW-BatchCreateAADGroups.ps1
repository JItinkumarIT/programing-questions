
# Connect to Azure AD
Connect-AzureAD

# Import the function script
. .\CreateAADGroups.ps1


# List of project names
$projectNames = @(
    "TSC Finance Calculation Engine",
    # Add more project names here
    "Another Project",
    "Yet Another Project"
)

# Loop through the project names and create groups
foreach ($projectName in $projectNames) {
    Write-Output "Processing project: $projectName"
    Create-ProjectGroups -ProjectName $projectName
}
