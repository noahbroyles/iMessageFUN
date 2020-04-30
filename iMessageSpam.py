import subprocess
from nlp import *


def runAppleScript(applescript, verbose=False):
    args = [item for x in [("-e", l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
    proc = subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)
    progname = proc.stdout.read().strip()
    if verbose:
        print(str(progname))


def sendList(listOfStrings: list, appleIDorPhone: str):
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
        runAppleScript(script)


if __name__ == "__main__":
    """To be called like so: python3 iMessageSpam.py --bible <phone number or apple ID>"""
    import sys

    args = sys.argv
    try:
        spam = [arg for arg in args if arg.startswith("--")][0]
    except IndexError:
        sys.exit("To be called like so: python3 iMessageSpam.py --bible <phone number or apple ID>")
    if len(args) == 1:
        print("Um... That doesn't work.")
    elif len(args) == 2:
        print("Please specify a phone number / apple ID to '" + spam.replace("--", '') + "'")
    elif len(args) == 3:
        appleID = args[-1]
        if spam == "--bible":
            sendList(getVerses("theBible.txt"), appleID)
