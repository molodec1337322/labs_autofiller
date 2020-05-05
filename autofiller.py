from docxtpl import DocxTemplate
from docxtpl import InlineImage
import os


def read_data(counter, program_text_folder_path, tasks_text_folder_path):

    source_text_filename = "task{0}.txt"
    source_program_text_filename = "task{0}.txt"

    with open(os.path.join(tasks_text_folder_path, source_text_filename.format(counter)), 'r', encoding='utf-8') as f:
        text = f.read()

    with open(os.path.join(program_text_folder_path, source_program_text_filename.format(counter)), 'r', encoding='utf-8') as f:
        program_text = f.read()

    return text, program_text


def fill_context(doc, counter, program_text_folder_path, tasks_text_folder_path, screenshots_folder_path):

    tasks_text, program_text = read_data(counter, program_text_folder_path,
                                         tasks_text_folder_path)

    context = {"task_number_{0}".format(counter): "Задача {0}".format(counter),
               "task_text_{0}".format(counter): tasks_text,
               "listing_name_{0}".format(counter): "Листинг{0} - задача номер {1}".format(counter, counter),
               "program_text_{0}".format(counter): program_text,
               "picture_{0}".format(counter): InlineImage(doc, os.path.join(screenshots_folder_path,
                                                                            "task{0}.png".format(counter))),
               "picture_text_{0}".format(counter): "Рисунок {0} - задача номер {1}".format(counter, counter)}

    return context


def main():

    new_filename = str(input("Введите название нового файла(без формата): "))
    new_filename += '.docx'

    program_text_folder_path = os.path.join(os.getcwd(), "program_text")

    tasks_text_folder_path = os.path.join(os.getcwd(), "tasks_text")

    screenshots_folder_path = os.path.join(os.getcwd(), "screenshots")


    title_filename = "template_labs.docx"
    doc = DocxTemplate(title_filename)

    counter = 1
    for i in range(12):
        doc.render(fill_context(doc, counter, program_text_folder_path,
                                tasks_text_folder_path, screenshots_folder_path))
        counter += 1

    doc.save(new_filename)


if __name__ == "__main__":
    main()

