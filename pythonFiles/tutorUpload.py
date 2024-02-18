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
        subjects = ["math", "biology", "physics", "chemistry", "english", "social studies"]
        topScore = 0
        topSubject = subjects[0]
        count = 15
        for line in lines[15:21]:
            if int(line) > int(topScore):
                topScore = line
                topSubject = subjects[count-15]
            count +=1
            scores.append(line)
            total += int(line)
        for x, score in enumerate(scores):
            scores[x] = int(score)*10/total
    
        file_content = f"""\
            ---
            layout: default
            modal-id: {lines[0]}
            email: {lines[3]}
            date: {lines[5]}
            fullName: {lines[6]}
            dob: {lines[7]}
            school: {lines[8]}
            grade: {lines[9]}
            phonenumber: {lines[11]}
            Signature: {lines[12]}
            ComfortwithMath: {lines[15]}
            ComfortwithBiology: {lines[16]}
            ComfortwithPhysics: {lines[17]}
            ComfortwithChemistry: {lines[18]}
            ComfortwithEnglish: {lines[19]}
            ComfortwithSocialStudies: {lines[20]}
            Vectorized Scores: {scores}
            project-date: {lines[21]}
            client: {lines[6]}
            img: cap{int(lines[0])%3+1}.jpg
            description: {lines[6]} at {lines[8]} with expertise in {topSubject}
            ---
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