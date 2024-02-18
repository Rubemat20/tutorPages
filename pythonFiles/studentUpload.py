import os
from datetime import date
from git import Repo
import openpyxl

def read_tutor_info_from_excel(file_path):
    tutor_info_list = []
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    for row in sheet.iter_rows(values_only=True):
        tutor_info = '\n'.join(str(cell) for cell in row)
        tutor_info_list.append(tutor_info.strip())
    return tutor_info_list
def create_markdown_files(tutor_info_list):
    today = date.today().strftime('%Y/%m/%d')
    file_names = []
    info_type = tutor_info_list[0]
    for i, tutor_info in enumerate(tutor_info_list[1:], start=1):
        lines = tutor_info.split('\n')
        tutor_name = lines[6].split(' ')[1]
        scores = []
        total = 0
        for line in lines[17:23]:
            scores.append(10-int(line))
            total += 10-int(line)
        if (len(lines)) < 24:
            lines.append("Monday")
        for x, score in enumerate(scores):
            scores[x] = int(score)*10/total
        file_content = f"""\
            ### Tutor Information

            - ID: {lines[0]}
            - Start time: {lines[1]}
            - Completion time: {lines[2]}
            - Email: {lines[3]}
            - Name: {lines[4]}
            - Last modified time: {lines[5]}
            - Full name: {lines[6]}
            - Date of birth: {lines[7]}
            - School: {lines[8]}
            - Grade: {lines[9]}
            - Phone number: {lines[10]}
            - Signature: {lines[11]}
            - Do you agree with attendance policy?: {lines[12]}
            - Do you agree with refund policy?: {lines[13]}
            - Any comments: {lines[14]}
            - Math Comfort Level: {lines[15]}
            - Biology Comfort Level: {lines[16]}
            - Physics Comfort Level: {lines[17]}
            - Chemistry Comfort Level: {lines[18]}
            - English Comfort Level: {lines[19]}
            - Social Studies Comfort Level: {lines[20]}
            - Vectorized Scores: {scores}
            - Dates: {lines[21]}
            """
        
        file_name = f'tutor_{tutor_name}.md'
        file_names.append(file_name)
        with open(file_name, 'w') as file:
            file.write(file_content)
    return file_names

def push_to_github(repo_path, file_names, commit_message):
    repo = Repo(repo_path)
    folder_path = "tutors"
    for file_path in file_names:
        new_file_path = os.path.join(folder_path, os.path.basename(file_path))
        try:
            os.rename(file_path, new_file_path)
        except FileExistsError:
            # Delete the existing file before renaming the new file
            os.remove(new_file_path)
            os.rename(file_path, new_file_path)
        # Add the moved file to the repository
        repo.index.add([new_file_path])
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def find_git_repo_directory():
    current_dir = os.getcwd()
    while True:
        if os.path.isdir(os.path.join(current_dir, '.git')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
        if current_dir == '/':
            raise FileNotFoundError("Git repository not found.")
            break
def main():
    # Define path to the Excel file containing tutor information
    excel_file_path = 'tutorinfo.xlsx'

    # Read tutor information from Excel file
    tutor_list = read_tutor_info_from_excel(excel_file_path)

    # Create Markdown file listing tutor information
    file_names = create_markdown_files(tutor_list)

    # Find the root directory of the Git repository
    repo_path = find_git_repo_directory()

    # Push Markdown files to GitHub
    push_to_github(repo_path, file_names, 'Add list of tutors')

if __name__ == "__main__":
    main()