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