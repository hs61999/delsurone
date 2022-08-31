import getpass, sys

#def question_and_answer(prompt):
#    print("Question: " + prompt)
#    msg = input()
#    print("Answer: " + msg)

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    if msg == "no":
        print("Bye!!")
    else:
        print("Let's go!!")        
    
def question_and_check(num, prompt, answer):
    print("Question " + str(num + 1) + ": " + prompt)    
    msg = input()

    correct_answer = 0
    if msg == answer:
        print(msg + " is correct!")
        correct_answer = 1
    else:
        print(msg + " is incorrect!")
        correct_answer = 0

    return correct_answer


questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")


questions = ["What command is used to include other functions that are developed?", \
    "What command in this example is used to evaluate a response?", \
    "Each 'if' command contains an '_________' to determine a true or false condition?"]

answers = ["import", "if", "expression"]

for i in range(0, len(questions)):
    #print(q)
    correct += question_and_check(i, questions[i], answers[i])

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(len(questions)))

exit()

rsp = question_with_response("What command is used to include other functions that are developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command in this example is used to evaluate a response?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))