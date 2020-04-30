import subprocess
from nlp import *


def runAppleScript(applescript):
    arguments = [item for x in [("-e", l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + arguments, stdout=subprocess.PIPE)
    proc.stdout.read()


def sendList(listOfStrings: list, appleIDorPhone: str, verbose=False):
    num = 1
    try:
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
            runAppleScript(script)
            if verbose:
                print("Sent {} spam message{} to {}".format(num, '' if num == 1 else "s", appleIDorPhone))
            num += 1
    except KeyboardInterrupt:
        print("Total spam messages sent to {}: {}".format(appleIDorPhone, num))
        sys.exit()


if __name__ == "__main__":
    options = """OPTIONS:
    -v (verbose)                    prints a tally of spam messages sent
    -c <number>                     specify a set number of messages to send
    --bible                         sends spam from the Word of God
    --random                        random crap spam
    -w --from-file <text file>      send each word in the specified file
    -s --from-file <text file>      send each sentence in the file
    -l --from-file <text file>      send each line in the file"""
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
        print("\n" + options + "\n")
    elif len(args) == 2:
        print("\n" + options + "\n")
    elif len(args) >= 3:
        appleID = args[-1]
        verbose = True if "-v" in args else False
        numberOfSpams = int(args[args.index("-c") + 1]) if "-c" in args else False
        if spam == "--bible":
            if numberOfSpams:
                sendList(getVerses("theBible.txt")[:numberOfSpams], appleID, verbose=verbose)
            else:
                sendList(getVerses("theBible.txt"), appleID, verbose=verbose)
        elif spam == "--random":
            if not numberOfSpams:
                numberOfSpams = random.randint(1, 1000)
            messages = []
            for _ in range(numberOfSpams):
                message = ''
                for __ in range(random.randint(10, 300)):
                    message += random.choice(list("\n" + string.ascii_letters + " "))
                messages.append(message)
            sendList(messages, appleID, verbose=verbose)
        elif spam == "--from-file":
            file = args[args.index("--from-file") + 1]
            if "-w" in args:
                if numberOfSpams:
                    sendList(getWords(file)[:numberOfSpams], appleID, verbose=verbose)
                else:
                    sendList(getWords(file), appleID, verbose=verbose)
            elif "-s" in args:
                if numberOfSpams:
                    sendList(getSentences(file)[:numberOfSpams], appleID, verbose=verbose)
                else:
                    sendList(getSentences(file), appleID, verbose=verbose)
            elif "-l" in args:
                if numberOfSpams:
                    sendList(getLines(file)[:numberOfSpams], appleID, verbose=verbose)
                else:
                    sendList(getLines(file), appleID, verbose=verbose)
