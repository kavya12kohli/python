#capitalize- makes the first letter of string uppercase
question="what are you doing here?"
x=question.capitalize()
print(x)

#casefold- makes all the characters lowercase
command="DO AS I SAY OR YOU WILL REGRET IT!"
x=command.casefold()
print(x)

#center- changes the string positioning
intro="My name is Kavya Kohli."
x=intro.center(88)
print(x)

#count- count the number of times a value appears in the string
statement="You know that I know and I know that you know as when you know, you know."
x=statement.count("know")
print(x)

#encode- encodes the string
french="Je parie que vous ne comprenez pas ce qui est écrit."
x=french.encode()
print(x)

#endswith- returns true if it ends with the specified value
numbers=("1,2,4,8,16")
x=numbers.endswith("4")
print(x)

#expandtabs- sets the tab size
exclaim="A\tm\ta\tz\ti\tn\tg\t!"
x=exclaim.expandtabs(11)
print(x)

#find- finds the first occurence of a value
sarcasm="No need to repeat yourself, I ignored you just fine the first time."
x=sarcasm.find("a")
print(x)

#format- inserts the specified value inside the string placeholder
enter=int(input("Enter your mobile number:"))
confirm="You entered:{number}"
print(confirm.format(number=enter))

#index- same as find
quote="Work hard in silence, let your success be your noise."
print(quote.index("silence"))

#isalnum- returns True if all values are alphanumeric
wannabe="Spice Girls"
print(wannabe.isalnum())

#isalpha- returns true if all values are alphabets without spaces
Alessia_Cara="Scars To Your Beautiful"
print(Alessia_Cara.isalpha())

#isascii- returns true if all characters are ascii
lovely="Billie Eilish, Khalid"
print(lovely.isascii())

#isdecimal- returns true if all values are decimal
Blackpink="How You Like That"
print(Blackpink.isdecimal())

#isdigit- returns true if all values are digits
mobile_number="76743536"
print(mobile_number.isdigit())

#isidentifier- returns true if string doesn't contain spaces or start with number
David_Guetta="Titanium"
print(David_Guetta.isidentifier())

#islower- returns true if all values are in lowercase
unimportant="pin"
print(unimportant.islower())

#isnumeric- same as isdigit
marks="99"
print(marks.isnumeric())

#isprintable- returns true if it is printable
stay="Zedd and Alessia Cara"
print(stay.isprintable())

#isspace- returns true if all characters are whitespace
blank="  "
print(blank.isspace())

#istitle- returns true if all values start with capital
Ava_Max="Kings And Queens"
print(Ava_Max.istitle())

#isupper- returns true if all characters are in upper case
Runaway="AURORA"
print(Runaway.isupper())

#join- takes all the iterable and turns them into one string
list=["party","fun","dance","food"]
x="->"
print(x.join(list))

#ljust- left align the string with a specific character
word="Feminism:"
x=word.ljust(17)
print(x,"It isn't about making women women strong, they already are. It is about changing the way the world perceives that strength." )

#lower- makes all characters lowercase
subject="PSYCHOLOGY"
print(subject.lower())

#lstrip- removes space to the left of string
songs="peace"
print("Listening to songs gives me ",songs.lstrip(),"unlike anything.")

#maketrans- replace specific characters
name="Navya"
x=name.maketrans("N","K")
print(name.translate(x))

#partition- splits the strings into a tuple with three elements
exhaustion="I really need a break right now."
print(exhaustion.partition("break"))

#replace- replaces a character with another
statement="I need to sleep now."
print(statement.replace("sleep","eat"))

#rfind- finds the last occurence of a particular character
word="assassination"
print(word.rfind("a"))

#rindex-same as rfind
word="sister"
print(word.rindex("s"))

#rjust- returns a right justified version of the string
word="Feminism:"
x=word.rjust(17)
print(x,"It isn't about making women women strong, they already are. It is about changing the way the world perceives that strength." )

#rpartition- same as partition
exhaustion="I really need a break right now."
print(exhaustion.rpartition("break"))

#rsplit- turns a string into a list
subjects="Maths, Physics, Chemistry"
print(subjects.rsplit("+"))

#rstrip-removes space to the right of the string
songs="peace"
print("Listening to songs gives me ",songs.rstrip(),"unlike anything.")

#split- splits the string into a list
python="Python is interesting."
print(python.split())

#splitlines- splits the string into a list at linebreak
polite="Thank you for the food\nIt was delicious"
print(polite.splitlines())

#startswith- opposite of endswith
Daya="Sit Still, Look Pretty"
print(Daya.startswith("Sit"))

#strip- removes the extra whitespace
songs="peace"
print("Listening to songs gives me ",songs.strip(),"unlike anything.")

#swapcase- lowercase switches with uppercase and viceversa
mantra="oM nAMAH sHIVAY"
print(mantra.swapcase())

#title- converts the first letter of every word into uppercase
exams="Prepare hard for exams or you will not get good marks."
print(exams.title())

#translate- returns the string where some specific characters are replaced
name="Navya"
x=name.maketrans("N","K")
print(name.translate(x))

#upper- makes all characters uppercase
excitement="I am so happy!"
print(excitement.upper())

#zfill- adds zero in the start of the string
num="100"
print(num.zfill(5))
