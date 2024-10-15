import json
import os
import random
import sys
    
def checkForFile(jsonPATH):
    if not (os.path.isfile(jsonPATH) and os.access(jsonPATH, os.R_OK)):
        print ("Either file is missing or is not readable, creating file...")
        with open(jsonPath, 'w') as optionFile:
            optionFile.write(json.dumps({}));
            
def loadJSONFile(jsonPath):
    with open(jsonPath, "r") as file:
        return json.load(file)["choices"];
        
def printOptions():
    print("---------------------------------");
    print("Welcome to the dinner randomiser!")
    print("---------------------------------");
    print("1. Add a dinner option");
    print("2. Remove a dinner option");
    print("3. Display dinner option(s)");
    print("4. Edit a dinner option");
    print("5. Randomise for a dinner option");
    print("6. Exit");
    
def isValidInput(input):
    validInput = ["1", "2", "3", "4", "5", "6", "exit"];
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
    
    itemToAdd = input("What option would you like to add: ").strip();
    # check if option is null or empty, return
    if itemToAdd == None or itemToAdd == "":
        print();
        return; 
    
    if optionIsInFile(choices, itemToAdd):
        print("Please add an option that does not exist in the file.\n");
    else:
        # add item to the file
        print("add");
    
def removeOption():
    print("remove");
    
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

def editOption():
    print("edit");
    
    
if __name__ == "__main__":
    # jsonPath = "dinner-randomiser/dinner-options.json";
    jsonPath = "dinner-options.json";
    ADD_OPTION = "1";
    REMOVE_OPTION = "2";
    DISPLAY_OPTION = "3";
    EDIT_OPTION = "4";
    RANDOMISE_OPTION = "5";
    QUIT_OPTION = "6";
    EXIT_OPTION = "exit";
    choices = [];
    
    checkForFile(jsonPath);
    choices = loadJSONFile(jsonPath);
        
    while True:
        printOptions();
        userInput = input("Select an option or exit: ");
        print();
        if isValidInput(userInput):
            if userInput == QUIT_OPTION or userInput.lower() == EXIT_OPTION:
                sys.exit();
            else:
                if userInput == ADD_OPTION:
                    addOption(choices);
                elif userInput == REMOVE_OPTION:
                    removeOption();
                elif userInput == DISPLAY_OPTION:
                    displayOption(choices);
                elif userInput == EDIT_OPTION:
                    editOption();
                else:
                    randomiseOption(choices);
        else:
            print("Please select a valid option.\n")
    

# things to do:
# create ingredient list for those items?