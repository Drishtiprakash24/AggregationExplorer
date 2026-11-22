from database import users_collection

# Display all users
users = users_collection.find()

for user in users:
    print(user)