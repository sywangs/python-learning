def greet_user(username = 'SYL'):
    """simple greet"""
    print ("Hello!" + username.title())

# greet_user()


def get_formatted_name(first_name,last_name,middle_name = ''):
    """return full name"""
    full_name = first_name + middle_name + last_name
    return full_name

# name = get_formatted_name("W","SY")
# print (name)


def build_person (first_name,last_name,middle_name = ''):
    """return disctionary"""
    person = {'first_name':first_name,'last_name':last_name}
    if middle_name :
        person['middle_name'] = middle_name
    return person


# person = build_person("W","SY","LL")
# print (person)

while True:
    print ("\n please tell me your name")
    print ("Enter 'q' to quit at any time")

    f_name = raw_input("First Name:")
    if f_name == 'q':
        break

    l_name = raw_input("Last Name:")
    if l_name == 'q':
        break

    full_name = get_formatted_name(f_name, l_name)
    print ("\nHello ," + full_name)
