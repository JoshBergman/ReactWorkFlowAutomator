import os


def getFileContents(projectDirectory):
    return f'''
    start cmd /k "cd {projectDirectory} & git log & git status"
    start cmd /k "cd {projectDirectory} & npm run start"
    start cmd /k "cd {projectDirectory} & npm run test"

    code
    '''


def createBatchFile(projectDirectory, saveDirectory, workflowTitle):
    bat_file_content = getFileContents(projectDirectory)

    directory = saveDirectory
    filename = f'{workflowTitle}.bat'

    file_path = os.path.join(directory, filename)

    with open(file_path, 'w') as bat_file:
        bat_file.write(bat_file_content)

    print(f"Workflow: {workflowTitle}, created successfully at {file_path}.")


saveDir = '''c:/Users/joshi/Desktop/WorkFlows'''  # Suggested use: just use save dir here, personally I just have folder on desktop with all my active workflows
# saveDir = input("Enter The Directory To Save Workflow At") # For those who save to a different location
projDir = input("Enter Directory For You Project: \n")
wrkflwTitle = input("Enter The Title For This Workflow: ")

createBatchFile(projDir, saveDir, wrkflwTitle)
