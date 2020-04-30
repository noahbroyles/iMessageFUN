# iMessage*FUN*
*A lil program for spamming via iMessage*  
This is a pretty cool little tool! Lots of things are possible with it. You can spam send bible verses to people, send utterly random texts to people, or send parts from a specified file to them(You could send a whole movie script one word at a time!)
<br>
<br>
## First Use:
First of all, it would be a good idea to install the requierments for the project:
```
pip3 install -r requierments.txt
```
Now you are ready to spam the daylights out of people!
<br>
<br>
## How to Run:
These are the options for the spammer:
```plaintext
-v (verbose)    prints a tally of spam messages sent
-c <number>     specify a set number of messages to send
--bible         sends spam from the Word of God
--random        sends random crap spam
-w --from-file <text file>     send each word in the specified file
-s --from-file <text file>     send each sentence in the file
-l --from-file <text file>     send each line in the file
```
So for example, running:
```
python3 iMessageSpam.py -v -c 2 --random <phone # or appleID>
```
would send 2 random messages to `<phone # or appleID>` and print:
```plaintext
Sent 1 spam message to 8633086227
Sent 2 spam messages to 8633086227
```

