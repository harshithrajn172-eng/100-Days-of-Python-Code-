PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter=letters.replace(PLACEHOLDER,strip_name)
        with open(f"./output/ReadyToSend/letter_for_{strip_name}.docx","w") as completed_letter:
            completed_letter.write(new_letter)
