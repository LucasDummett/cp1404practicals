"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """ Read subject information and print in an organised format."""
    subject_details = load_subject_details(FILENAME)
    print_subject_details(subject_details)


def load_subject_details(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []  # Named subject details as it will be a nested list.
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_details.append(parts)
    input_file.close()
    return subject_details


def print_subject_details(subject_details):
    """Print subject details in an organised format."""
    for subject_detail in subject_details:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:12} and has {subject_detail[2]:3} students")


main()

