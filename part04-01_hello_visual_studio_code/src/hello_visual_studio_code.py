# Write your solution here
editor = "Visual Studio Code"
editor_choice = input("Editor:")
while True:
    if  editor_choice.lower() == editor.lower():
        print("an excellent choice!")
        break
    if editor_choice.lower() == "emacs" or editor_choice.lower() == "vim" or editor_choice.lower() == "atom":
        print("not good")
        editor_choice = input("Editor:")
    if editor_choice.lower() == "notepad" or editor_choice.lower() == "word":
        print("awful")
        editor_choice = input("Editor:")
        