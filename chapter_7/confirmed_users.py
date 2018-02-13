unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    confirmed_users.append(user)

print("\n The following users have been confirmed")
for user in confirmed_users:
    print(user)

