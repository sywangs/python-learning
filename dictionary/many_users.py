
# define nested dic
users = {
    'aeinstein':{
        'first':'albert',
        'last':'esnstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'cuire',
        'location':'paris',
    }
}

#access to the dic inside
for user_name,user_value in users.items():
    print (user_name + ":")
    full_name = user_value['first'] + " " + user_value['last']
    location = user_value['location']
    print ("\tfull Name:" + full_name)
    print ("\tlocation:" + location)