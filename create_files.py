import os


def create_files(count, path, filename):

    for i in range(count):
        if os.path.exists(os.path.join(path, filename.format(i + 1))) is False:
            with open(os.path.join(path, filename.format(i + 1)), 'tw') as f:
                pass


def main():

    files_count = 12

    program_text_folder_path = os.path.join(os.getcwd(), "program_text")
    create_files(files_count, program_text_folder_path, "task{0}.txt")

    tasks_text_folder_path = os.path.join(os.getcwd(), "tasks_text")
    create_files(files_count, tasks_text_folder_path, "task{0}.txt")

    screenshots_folder_path = os.path.join(os.getcwd(), "screenshots")
    create_files(files_count, screenshots_folder_path, "task{0}.png")


if __name__ == "__main__":
    main()