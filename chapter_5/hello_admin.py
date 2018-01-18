current_users = ['luke', 'colin', 'edel', 'chloe', 'isabelle']
new_users = ['johanna', 'edel', 'stephanie', 'ciaran', 'Chloe']

for user in new_users:
    if user.lower() in current_users:
        print(user + " already exists")
    else:
        print(user + " user name is available")