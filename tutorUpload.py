import os
from datetime import date
from git import Repo

def read_tutor_info(folder_path):
    tutor_info_list = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                tutor_info = file.read()
                tutor_info_list.append(tutor_info.strip())
    return tutor_info_list

def increment_modal_id(tutor_info_list):
    new_tutor_info_list = []
    for i, tutor_info in enumerate(tutor_info_list, start=1):
        new_tutor_info = tutor_info.replace('modal-id: 6', f'modal-id: {i}')
        new_tutor_info_list.append(new_tutor_info)
    return new_tutor_info_list

def generate_image_filename(tutor_name):
    first_name = tutor_name.split()[0].lower()  # Assuming tutor name is in the format "First Last"
    return f'{first_name}.png'

def create_markdown_files(tutor_info_list):
    today = date.today().strftime('%Y/%m/%d')
    file_names = []
    for i, tutor_info in enumerate(tutor_info_list, start=1):
        lines = tutor_info.split('\n')
        tutor_name = lines[6].split(': ')[1]
        lines[1] = f"modal-id: {i}"
        lines[2] = f"date: {today}"
        lines[3] = f"img: {generate_image_filename(tutor_name)}"
        lines[8] = f"subject(s): {lines[8].split(': ')[1]}"  # Assuming subject(s) field is already in the correct format
        file_names.append(f'tutor_{i}.md')
        with open(f'tutor_{i}.md', 'w') as file:
            file.write('\n'.join(lines))
    return file_names
def push_to_github(repo_path, file_names, commit_message):
    repo = Repo(repo_path)
    for file_path in file_names:
        repo.index.add([file_path])
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def main():
    # Define folder containing .txt files
    folder_path = 'folder_of_txt_files'

    # Read student names from .txt files
    tutor_list = read_tutor_info(folder_path)

    # Create Markdown file listing student names
    file_names = create_markdown_files(tutor_list)
    current_dir = os.getcwd()
    repo_path = None
    while True:
        # Check if the .git directory exists in the current directory
        if os.path.isdir(os.path.join(current_dir, '.git')):
            repo_path = current_dir
            break
        # Move up one directory
        current_dir = os.path.dirname(current_dir)
        # Stop if we've reached the root directory
        if current_dir == '/':
            break

    # Push Markdown file to GitHub
    push_to_github(repo_path, file_names, 'Add list of tutors')

if __name__ == "__main__":
    main()