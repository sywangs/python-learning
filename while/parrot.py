# message = raw_input("Tell me a secret,I won't tell it to anyone..:")
# print (message)


prompt = "\n Tell me somthing ,I won't tell it to anyone:\n"
prompt += "Enter 'quit' to end your input."
message = ""

while message.find("quit") == -1:
    message += raw_input(prompt)
    print ("I am going to keep this secret...")

message = message.strip('quit')
print ("\nSceret Publish ahah!!!" + message + "")