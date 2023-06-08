import os

template_file = "template.txt"
recipients_file = "employees.txt"
output_directory = "christmasCards"

with open(template_file, "r") as file:
    template_content = file.read()

with open(recipients_file, "r") as file:
    names = file.read().splitlines()

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for name in names:
    card_content = template_content.replace("NAME", name)
    file_name = f"{name}.txt"
    with open(os.path.join(output_directory, file_name), "w") as file:
        file.write(card_content)