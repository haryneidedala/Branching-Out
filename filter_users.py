import json
import json

def filter_by_age(data, min_age, max_age):
    """Filters users by age range."""
    return [user for user in data if min_age <= user['age'] <= max_age]

# Load data from users.json
with open('users.json') as f:
    users = json.load(f)

# Example usage:
filtered_users = filter_by_age(users, 20, 30)  # Gets users aged 20-30
print(filtered_users)

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")

