import subprocess
from Treehacks_matching_algo.session import *
from Treehacks_matching_algo.matching import *
import os

def get_file_paths(folder_path, file_extension):
    """
    Retrieve file paths in the given folder with the specified file extension
    """
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))
    return file_paths

def read_specific_lines(file_paths, line_numbers):
    """
    Read specific lines from files and return as a list of strings
    """
    file_contents = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            selected_lines = [line.split(": ", 1)[-1].strip() for i, line in enumerate(lines, start=1) if i in line_numbers]
            file_contents.append(selected_lines)
    return file_contents


def main():
    # Define the list of Python scripts in the order you want to execute them
    scripts = ["studentUpload.py", "tutorUpload.py"]
    # Iterate over the scripts and execute them one by one
    for script in scripts:
        print(f"Running script: {script}")
        try:
            subprocess.run(["python", script], check=True)
            print(f"Script {script} executed successfully.")
        except subprocess.CalledProcessError:
            print(f"Error occurred while executing {script}. Exiting pipeline.")
            break
    # Paths to tutors and students folders
    tutors_folder_path = "tutors"
    students_folder_path = "students"

    # Get paths to tutor.md and student.md files
    tutor_files = get_file_paths(tutors_folder_path, ".md")
    student_files = get_file_paths(students_folder_path, ".md")

    # Define the line numbers you want to read
    tutor_lines_to_read = [5, 8, 9, 3, 17, 18, 2]  # Example: Read the 1st, 3rd, and 5th lines
    student_lines_to_read = [5, 9, 3, 17, 18, 2, 8]  # Example: Read the 2nd, 4th, and 6th lines

    # Read specific lines from tutor and student files
    tutors_info = read_specific_lines(tutor_files, tutor_lines_to_read)
    students_info = read_specific_lines(student_files, student_lines_to_read)

    # Call the matching function with tutors and students information
    res = matching(tutors_info, students_info)

    print(res)
    return res
    

if __name__ == "__main__":
    main()
