n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:  #Infinite loop: The loop does not increment the "Loading" variable, so "loading module" will continue forever
        print("Loading module " + str(loading))
        loading +=1 #Bug 1 fix: The loop will no longer be infinite
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #Syntax Error, Bug 2 fix: should be double equals sign
            print("Current Crew List:")
            
            for i in range(len(n)): #Index error: loops until it reaches 10, so the code crashes once it reaches 4. Bug 3 fix.
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank) #Bug 4 fix: Keeps the data in sync
            r.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            if rem in n: #Bug 5 fix: Checks in the name exists to avoid any value errors
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:   #Bug 6 fix: Added an else function to stop the code crashing
                print("Name not found")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": #Bug 7 fix: Corrected logical comparison
                    count = count + 1
            print("High ranking officers: " + str(count)) #Bug 8 fix: Cast count to string to avoid TypeError
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            fuel -= 50 #Bug 9 Fix: Fuel actually decreases now
            break 
            
        print("End of cycle.")

run_system_monolith() #Bug 10 fix: Added parentheses to call the function