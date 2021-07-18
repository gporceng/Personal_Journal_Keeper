import os
global path
directory = "Library"
parent_dir = "/home/gp3/Projects/Personal_Journal_Keeper/"
path = os.path.join(parent_dir,directory)

class Assistant:
    name = "Brigid"

    def speak(self, words):
        print(self.name + ": " + words)


global bot
bot = Assistant()

def newNote():

    lines = []
    line = ""
    while(line != ("STOP " + bot.name.upper())):
        line = input()
        lines.append(line)
    print("What would you like to save this file as?")
    output_filename = input()
    output_file = open(output_filename, "w")

    for row in lines:
        output_file.write(row + "\n")
    output_file.close()


def start_convo():
    bot.speak("Hello Greg! Hope you're having a nice day. How can I help?")
    bot.speak("Can I...?:")
    print(" 1. WRITE: add a new thought\n  2. READ: print out a searched result")

    resp = input("Your Response: ")
    if(resp == "1"):
        bot.speak("Please start typing your new note, and when you would like to end print: STOP " + bot.name.upper()+"\n\nNew Note:") 
        newNote()

def login():
    try:
        os.mkdir(path)
    except OSError as error:
        print("Successfully Established Library:")
        start_convo()

def main():
    login()

main()