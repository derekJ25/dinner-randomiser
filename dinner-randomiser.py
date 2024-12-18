import json
import os
import random
import sys
import constants
    
def checkForFile(jsonPATH):
    if not (os.path.isfile(jsonPATH) and os.access(jsonPATH, os.R_OK)):
        print ("Either file is missing or is not readable, creating file...")
        with open(jsonPath, 'w') as optionFile:
            optionFile.write(json.dumps({}));
            
def loadJSONFile(jsonPath):
    with open(jsonPath, "r") as file:
        return json.load(file)["choices"];
    
def saveJSONFile(jsonPath, choices):
    with open(jsonPath, "w") as file:
        options = {
            "choices": choices
        }
        file.write(json.dumps(options));
        
def printOptions():
    print("---------------------------------");
    print("Welcome to the dinner randomiser!")
    print("---------------------------------");
    print("1. Add a dinner option");
    print("2. Remove a dinner option");
    print("3. Display dinner option(s)");
    print("4. Edit a dinner option");
    print("5. Randomise for a dinner option");
    print("6. Save & Exit");
    print("7. Exit");
    
def isValidInput(input):
    validInput = ["1", "2", "3", "4", "5", "6", "7", "exit"];
    return True if input.lower() in validInput else False;

def optionIsInFile(choices, optionToAdd):
    for item in choices:
        if item.lower().strip() == optionToAdd.lower():
            return True;
    return False;

def randomiseOption(choices):
    if len(choices) > 0:
        print(f"The randomiser has selected: {choices[random.randint(0, len(choices) - 1)]}");
    else:
        print("There are no options stored. Please add an option.")
        
def addOption(choices):
    displayOption(choices);
    
    itemToAdd = input("What option would you like to add (Hit enter to go back): ").strip().lower().capitalize();
    if itemToAdd == None or itemToAdd == "":
        print("\nReturning to menu.\n");
        return; 
    
    if optionIsInFile(choices, itemToAdd):
        print("\nPlease add an option that does not exist in the file.\n");
    else:
        choices.append(itemToAdd);
        print(f'\n{itemToAdd} has been added to the dinner options.\n')
        
def removeOption(choices):
    displayOption(choices);
    removeOption = input("Which option would you like to remove (Hit enter to go back): ").strip().lower().capitalize();
    if removeOption == None or removeOption == "":
        print("\nReturning to menu.\n");
        return; 
    
    if(optionIsInFile(choices, removeOption)):
        choices.remove(removeOption);
        print(f'\n{removeOption} has been removed from the dinner options.\n');
    else:
        print(f'\n{removeOption} is not a dinner option in system.\n');

def editOption(choices):
    displayOption(choices);
    editItem = input("What option would you like to edit? ").strip().lower().capitalize();
    if editItem == None or editItem == "":
        print("\nReturning to menu.\n");
        return; 
    
    if(optionIsInFile(choices, editItem)):
        print(f'\nEditing option: {editItem}');
        newItemName = input(f'What would you like {editItem} now be called? ');
        choices[choices.index(editItem)] = newItemName;
        print(f'\nSuccessfully changed {editItem} to {newItemName}.\n');
    else:
        print(f'\n{editItem} does not exist as an option.\n');
        
def displayOption(choices):
    if len(choices) > 0:
        print("---------------------------------");
        print("Displaying dinner choices");
        print("---------------------------------");
        for choice in choices:
            print(choice.capitalize());
        print();
    else:
        print("Sorry. There is nothing to display.")
    
if __name__ == "__main__":
    # jsonPath = "dinner-randomiser/dinner-options.json";
    jsonPath = "dinner-options.json";
    
    choices = [];
    
    checkForFile(jsonPath);
    choices = loadJSONFile(jsonPath);
        
    while True:
        printOptions();
        userInput = input("Select an option or exit: ");
        print();
        if isValidInput(userInput):
            if userInput == constants.QUIT_OPTION or userInput.lower() == constants.EXIT_OPTION or userInput == constants.SAVE_EXIT_OPTION:
                if userInput == constants.SAVE_EXIT_OPTION:
                    print("Saving dinner choices to file.");
                    saveJSONFile(jsonPath, choices);
                print("Program is shutting down.");
                sys.exit();
            else:
                if userInput == constants.ADD_OPTION:
                    addOption(choices);
                elif userInput == constants.REMOVE_OPTION:
                    removeOption(choices);
                elif userInput == constants.DISPLAY_OPTION:
                    displayOption(choices);
                elif userInput == constants.EDIT_OPTION:
                    editOption(choices);
                else:
                    randomiseOption(choices);
        else:
            print("Please select a valid option.\n");
    

# things to do:
# create ingredient list for those items?