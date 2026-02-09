#Function 1:
def init_database():
    names = ["Jean Picard", "William Riker", "Worf", "Deanna Troi", "Geordi La Froge"] #5 Star trek character
    ranks = ["Capitain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Operations", "Engineering", "Security", "Sciences"]
    ids = ["NCC-1701-01", "NCC-1701-02", "NCC-1701-03", "NCC-1701-04", "NCC-1701-05"]
    return names, ranks, divs, ids

#Function 2:
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


#Function 3:
def add_member(names, ranks, divs, ids):
    #Validates ID is unique
    valid_ranks = ["Capitan", "Commander", "Lt. Commander", "Lieutendant", "Lt. Junior Grade", "Ensign"]
    new_id = input("Enter unique ID: ")
    if new_id in ids:
        print("Error: ID already exists")
        return
    # Validates rank is a valid TGN rank
    new_rank = input("Enter Rank: ")
    if new_rank not in valid_ranks:
        print("Error: Invalid TNG rank")
        return
    
    new_name = input("Enter Name: ")
    new_div = input("Enter Division: (Command, Operations, Sciences, Engineering, Security): ")
#Appends Data to all 4 lists
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("**Member added successfully**")


#Function 4:
def remove_member(names, ranks, divs, ids):
    rem_id = input("Enter ID of member to remove: ") #Asks user for ID
    if rem_id in ids:  #Finds the Index
        idx = ids.index(rem_id)
        #Removes entry from all 4 lists to keep them in sync
        names.pop(idx)  
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member removed from all systems")
    else:
        print("Error: ID was not found")

#Function 5:
def update_rank(names, ranks, ids):
    upd_id = input("Enter ID to update rank: ")
    if upd_id in ids:      #Finds a member by ID
        idx = ids.index(upd_id)   #Updates their rank string
        new_rank = input("Enter new rank for " + names[idx] + ":")
        ranks[idx] = new_rank
        print("Rank updated!")
    else:
        print("Error: ID was not found")



#Function 6:

def display_roster(names, ranks, divs, ids):
    #iterates through the lists





#Function 7:
def search_crew(names,ranks,divs,ids):
    term = input("Enter name to search for: ").lower()
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"Match for: {names[i]}, {ranks[i]}, {divs[i]}, {ids[i]}")


#Function 8:
def filter_by_division(names,divs):
    division = input("Enter division to filter (Command, Operations, Sciences): ")
    print(f"Crew in {div_choice}: ")
    for i in range(len(names)):
        if divs[i] == division:
            print(f"{names[i]}")


#Function 9:
def calculate_payroll(ranks):
    credit_value = 0
    if rank == "Captain":
        credit_value += 1000
    elif rank == "Commander":
        credit_value += 750
    elif rank == "Lt. Commander":
        credit_value += 650
    elif rank == "Lieutenant":
        credit_value += 500
    else:
        credit_value += 250
    return credit_value
