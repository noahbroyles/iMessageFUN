import subprocess
from nlp import *


def runAppleScript(applescript, verbose=False):
    args = [item for x in [("-e", l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)
    progname = proc.stdout.read().strip()
    if verbose:
        print(str(progname))


def sendList(listOfStrings: list, appleIDorPhone: str, verbose=False):
    for message in listOfStrings:
        # Leyla is the inspiration for this program, FYI ;)
        script = '''
        on run
        	tell application "Messages"
        		set iMessageService to 1st service whose service type = iMessage
        		set leyla to buddy "''' + appleIDorPhone + '''" of iMessageService
        		send "''' + message + '''" to leyla
        	end tell
        end run'''
        if verbose:
            runAppleScript(script, verbose=True)
        else:
            runAppleScript(script)


if __name__ == "__main__":
    """To be called like so: python3 iMessageSpam.py --bible <phone number or apple ID>"""
    """OPTIONS: -c <count>
                -v (verbose) 
                --bible 
                --random 
                --from-file <file>"""
    import sys
    import random
    import string

    args = sys.argv
    try:
        spam = [arg for arg in args if arg.startswith("--")][0]
    except IndexError:
        sys.exit("Ya did it wrong.")
    if len(args) == 1:
        print("Um... That doesn't work.")
    elif len(args) == 2:
        print("Please specify a phone number / apple ID to '" + spam.replace("--", '') + "'")
    elif len(args) >= 3:
        appleID = args[-1]
        if spam == "--bible":
            if "-c" in args:
                amount = int(args[args.index("-c") + 1])
                if "-v" in args:
                    sendList(getVerses("theBible.txt")[:amount], appleID, verbose=True)
                else:
                    sendList(getVerses("theBible.txt")[:amount], appleID)
            else:
                if "-v" in args:
                    sendList(getVerses("theBible.txt"), appleID, verbose=True)
                else:
                    sendList(getVerses("theBible.txt"), appleID)
        if spam == "--random":
            if "-c" not in args:
                amount = random.randint(1, 1000)
            else:
                amount = int(args[args.index("-c") + 1])
            messages = []
            for _ in range(amount):
                message = ''
                for __ in range(random.randint(10, 300)):
                    message += random.choice(list("\n" + string.ascii_letters + " "))
                messages.append(message)
            if "-v" in args:
                sendList(messages, appleID, verbose=True)
            else:
                sendList(messages, appleID)
