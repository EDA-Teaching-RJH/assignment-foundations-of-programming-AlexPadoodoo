def init_database():
    names = ["Jean Picard", "William Riker", "Worf", "Deanna Troi", "Geordi La Froge"] #5 Star trek character
    ranks = ["Capitain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Operations", "Engineering", "Security", "Sciences"]
    ids = ["NCC-1701-01", "NCC-1701-02", "NCC-1701-03", "NCC-1701-04", "NCC-1701-05"]
    return names, ranks, divs, ids


def display_menu(user_name):
    print("\n" + "="*30)
    print("FLEET MANAGEMENT SYSTEM")
    print("--------------------------")
    print(f"Logged in as: " + user_name)
    print("="*30)
    print("1. View Roaster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Divison")
    print("7. Calculate Payroll")
    print("8. Count Senior Officers")
    print("9. Exit")

    choice = input("\n Select an option (1-9): ")
    return choice

def add_member(names, ranks, divs, ids):
    valid_ranks = ["Capitan", "Commander", "Lt. Commander", "Lieutendant", "Lt. Junior Grade", "Ensign"]
    new_id = input("Enter unique ID: ")
    if new_id in ids:
        print("Error: ID already exists")
        return
    new_rank = input("Enter Rank: ")
    if new_rank not in valid_ranks:
        print("Error: Invalid TNG rank")
        return
    
    new_name = input("Enter Name: ")
    new_div = input("Enter Division: (Command, Operations, Sciences, Engineering, Security): ")

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("**Member added successfully**")

def remove_member(names, ranks, divs, ids):
    rem_id = input("Enter ID of member to remove: ")
    if rem_id in ids:
        idx = ids.index(rem_id)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member removed from all systems")
    else:
        print("Error: ID was not found")

def update_rank(names, ranks, ids):
    upd_id = input("Enter ID to update rank: ")
    if upd_id in ids:
        idx = ids.index(upd_id)
        new_rank = input("Enter new rank for " + names[idx] + ":")
        ranks[idx] = new_rank
        print("Rank updated!")
    else:
        print("ErrorL ID was not found")

