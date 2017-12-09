#define dic
alien_0 = {'color':'green','points':5}

#access value of dic
print(alien_0['color'])
print(alien_0['points'])

#add key value
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
#modify value
alien_0['color'] = 'yellow'
print(alien_0)

#delete key,value
del alien_0['points']
print (alien_0)

#traersing dic
for key,vlaue in alien_0.items():
    print("\nkey:" + key)
    print ("value:" + str(vlaue))

