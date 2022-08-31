InfoDb = []

# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "Delsurone",
    "LastName": "K",
    "DOB": "Dec 7",
    "Residence": "San Diego",
    "Email": "delsurone@poway.org",
    "Owns_Cars": ["2016-Honda", "2013-Lexus", "2003-Toyota", "1997-Volvo", "1969-GMC"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Srudeleon",
    "LastName": "K",
    "DOB": "Mar 13",
    "Residence": "Atlanta",
    "Email": "srudeleon@poway.org",
    "Owns_Cars": ["2005-Accura", "2012-MINI"]
})

# Print the data structure
#print(InfoDb)


# print function: given a dictionary of InfoDb content
def print_data(d_rec):
    print(d_rec["FirstName"], d_rec["LastName"])  # using comma puts space between values
    print("\t", "Residence:", d_rec["Residence"]) # \t is a tab indent
    print("\t", "Birth Day:", d_rec["DOB"])
    print("\t", "Cars: ", end="")  # end="" make sure no return occurs
    print(", ".join(d_rec["Owns_Cars"]))  # join allows printing a string list with separator
    print()


# for loop algorithm iterates on length of InfoDb
def for_loop():
    print("For loop output\n")
    for record in InfoDb:
        print_data(record)

#for_loop()

# while loop algorithm contains an initial n and an index incrementing statement (n += 1)
def while_loop():
    print("While loop output\n")
    i = 0
    while i < len(InfoDb):
        record = InfoDb[i]
        print_data(record)
        i += 1
    return

#while_loop()

# recursion algorithm loops incrementing on each call (n + 1) until exit condition is met
def recursive_loop(i):
    if i < len(InfoDb):
        record = InfoDb[i]
        print_data(record)
        recursive_loop(i + 1)
    return
    
#print("Recursive loop output\n")
#recursive_loop(0)

###############################################################################
# Try to do a for loop with an index
def for_loop2():
    print("For loop output\n")
    for idx in range(len(InfoDb)):
        print_data(InfoDb[idx])

#for_loop2()

###############################################################################
# Would it be possible to output data in a reverse order?
def for_loop3():
    print("For loop output\n")
    for idx in range(len(InfoDb) - 1, -1, -1):
        print_data(InfoDb[idx])

#for_loop3()

###############################################################################
# Could you create new or add to dictionary data set? Could you do it with input?
def print_data2(d_rec):
    print(d_rec["FirstName"], d_rec["LastName"])  # using comma puts space between values
    print("\t", "School Name:", d_rec["SchoolName"]) # \t is a tab indent
    print("\t", "Grade:", d_rec["Grade"])
    print()

# Keys for new DB
NewInfoDbKeys = ["FirstName", "LastName", "SchoolName", "Grade"]

NewInfoDb = []

while (1):
    print()
    TempDict = {}  # temp dictionary 
    for Keys in NewInfoDbKeys:
        print("Please type " + Keys)
        userInput = input()
        TempDict[Keys] = userInput
    NewInfoDb.append(TempDict)  # add a dictionary  
    
    # ask user to continue
    print("Do you want to continue?")
    userInput = input()
    if userInput != 'yes':
        print("Ok we will stop\n")
        break
    else:
        print("\nPut next info")

def for_loop4():
    for idx in range(len(NewInfoDb)):
        print_data2(NewInfoDb[idx])
for_loop4()

###############################################################################
# Make a quiz that stores in a List of Dictionaries.
# See 2022-08-28-quiz_3.py    