import subprocess
from nlp import *


def runAppleScript(applescript, verbose=False):
    args = [item for x in [("-e", l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)
    progname = proc.stdout.read().strip()
    if verbose:
        print(str(progname))


def sendList(listOfStrings: list, appleIDorPhone: str, verbose=False):
    for m in listOfStrings:
        # Leyla is the inspiration for this program, FYI ;)
        script = '''
        on run
        	tell application "Messages"
        		set iMessageService to 1st service whose service type = iMessage
        		set leyla to buddy "''' + appleIDorPhone + '''" of iMessageService
        		send "''' + m + '''" to leyla
        	end tell
        end run'''
        if verbose:
            runAppleScript(script, verbose=True)
        else:
            runAppleScript(script)


if __name__ == "__main__":
    options = """OPTIONS:
    -c <number of messages to send>
    -v (verbose) 
    --bible 
    --random 
    --from-file <text file>
        -w  send each word in the specified file
        -s  send each sentence in the file
        -l  send each line in the file"""
    import sys
    import random
    import string

    args = sys.argv
    try:
        spam = [arg for arg in args if arg.startswith("--")][0]
    except IndexError:
        print("\n" + options + "\n")
        sys.exit()
    if len(args) == 1:
        print("Um... That doesn't work.")
    elif len(args) == 2:
        print("Please specify a phone number / apple ID to '" + spam.replace("--", '') + "'")
    elif len(args) >= 3:
        appleID = args[-1]
        verbose = True if "-v" in args else False
        amount = int(args[args.index("-c") + 1]) if "-c" in args else False
        if spam == "--bible":
            if amount:
                sendList(getVerses("theBible.txt")[:amount], appleID, verbose=verbose)
            else:
                sendList(getVerses("theBible.txt"), appleID, verbose=verbose)
        elif spam == "--random":
            if not amount:
                amount = random.randint(1, 1000)
            messages = []
            for _ in range(amount):
                message = ''
                for __ in range(random.randint(10, 300)):
                    message += random.choice(list("\n" + string.ascii_letters + " "))
                messages.append(message)
            sendList(messages, appleID, verbose=verbose)
        elif spam == "--from-file":
            file = args[args.index("--from-file") + 1]
            if "-w" in args:
                sendList(getWords(file), appleID, verbose=verbose)
            elif "-s" in args:
                sendList(getSentences(file), appleID, verbose=verbose)
            elif "-l" in args:
                sendList(getLines(file), appleID, verbose=verbose)
