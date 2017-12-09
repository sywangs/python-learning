def build_user_profile(first,last,*hobbies,**user_info):
    user = {}
    user['first_name'] = first
    user['last_name'] = last
    user['hobbies'] = hobbies
    for key,value in user_info.items() :
        user[key] = value
    return user

user = build_user_profile("W","SY","swimmming","hiking","running",location='princeton', field='physics')
print (user)
