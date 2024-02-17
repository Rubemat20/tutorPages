import os
from datetime import date

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
    for i, tutor_info in enumerate(tutor_info_list, start=1):
        lines = tutor_info.split('\n')
        tutor_name = lines[6].split(': ')[1]
        lines[1] = f"modal-id: {i}"
        lines[2] = f"date: {today}"
        lines[3] = f"img: {generate_image_filename(tutor_name)}"
        lines[8] = f"subject(s): {lines[8].split(': ')[1]}"  # Assuming subject(s) field is already in the correct format
        with open(f'tutor_{i}.md', 'w') as file:
            file.write('\n'.join(lines))

def main():
    # Define folder containing .txt files
    folder_path = 'tutors'

    # Read tutor information from .txt files
    tutor_info_list = read_tutor_info(folder_path)

    # Increment modal-id and update other fields
    updated_tutor_info_list = increment_modal_id(tutor_info_list)

    # Create Markdown files with updated information
    create_markdown_files(updated_tutor_info_list)

if __name__ == "__main__":
    main()
