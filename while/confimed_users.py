# unconfirmed user list
unconfirmed_users = ['alice','brain','candace']
#confirmed users
confirmed_users = []

#verify elements one by one
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print ("Verifying user;" + current_user.title())
    confirmed_users.append(current_user)

print ("the following users hava been confirmed:")
for user in confirmed_users:
    print (user.title())