# iMessage*FUN*
*A lil program for spamming via iMessage*  
<br>
This is a pretty cool little tool! Lots of things are possible with it. You can spam send bible verses to people, send utterly random texts to people, or send parts from a specified file to them. You could send a whole movie script one word at a time!  
This **ONLY WORKS ON MACOS** by the way, since iMessages and AppleScript are Apple things. Linux bros, I'm sorry. I can't help it. Windows people get lost.
<br>
<br>
## First Use:
First of all, install the requirements for the project:
```
pip3 install -r requirements.txt
```
Now you are ready to spam the daylights out of people!
<br>
<br>
## How to Run:
These are the options for the spammer:
```plaintext
-v (verbose)                    prints a tally of the number of spam messages sent
-c <number>                     specify a set number of messages to send
--bible                         sends spam from the Word of God
--random                        sends random crap spam
-w --from-file <text file>      send each word in the specified file
-s --from-file <text file>      send each sentence in the file
-l --from-file <text file>      send each line in the file
```
Now in order for the spammer to work, the Messages app has to be *open* on your Mac, and there needs to be an existing chat with the person you are targeting. If either of these conditions are not met, 
you will see something nasty like
```commandline
151:330: execution error: Messages got an error: Can’t get buddy id "74E7EF7C-DFEB-425F-91E5-1847C90995B3:<phone# or appleID>". (-1728)
```  
Well, now you know what that is.
So for example, running:
```commandline
python3 iMessageSpam.py -vc 2 --random <phone# or appleID>
```
would send 2 random messages to `<phone# or appleID>` and print:
```plaintext
Sent 1 spam message to <phone# or appleID>
Sent 2 spam messages to <phone# or appleID>
```
because it's in verbose mode. Running:
```commandline
python3 iMessageSpam.py --bible <phone# or appleID>
```
would send as many verses are are in the bible to `<phone# or appleID>` silently, or stop when you press `Ctrl-C`.  
```commandline
python3 iMessageSpam.py -vl --from-file README.md <phone# or appleID>
```
would send each line from `README.md`(this file) to `<phone# or appleID>`, _and_ tell you as it sends.
