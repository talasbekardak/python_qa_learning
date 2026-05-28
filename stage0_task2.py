users = [
      {"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25},
      {"name": "Carol", "age": 28},
  ]
user2= []
users3 = {}
for user in users:
    if(user["age"] > 27):
        user2.append(user)
print(user2)

for user in users:
    users3[user["name"]] = user["age"]
print(users3)

