# Function to display candidates and their vote counts
def display_candidates(candidates):
    print("\nCandidates and their current vote counts:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to allow users to vote
def vote(candidates, voters):
    user_id = input("Enter your ID: ")
    
    if user_id in voters:
        print("You have already voted. You cannot vote again.")
        return
    
    # Display candidates to the user
    display_candidates(candidates)
    
    # Ask the user to vote for a candidate
    while True:
        try:
            choice = input(f"Hello {user_id}, please choose a candidate to vote for (or type 'exit' to cancel): ").strip()
            if choice.lower() == 'exit':
                print("Exiting the vote selection.")
                return
            if choice not in candidates:
                raise ValueError("Invalid candidate choice. Please choose a valid candidate.")
            
            # Add the vote
            candidates[choice] += 1
            voters.add(user_id)  # Add the user to the voted set
            print(f"Thank you for voting for {choice}!")
            return
        except ValueError as e:
            print(e)

# Function to view results (admin only)
def view_results(candidates, admin_password):
    password = input("Enter admin password to view results: ")
    if password == admin_password:
        display_candidates(candidates)
    else:
        print("Incorrect password. Access denied.")

# Function to reset votes (admin only)
def reset_votes(candidates, voters, admin_password):
    password = input("Enter admin password to reset votes: ")
    if password == admin_password:
        for candidate in candidates:
            candidates[candidate] = 0
        voters.clear()
        print("Voting has been reset.")
    else:
        print("Incorrect password. Access denied.")

# Main program loop
def main():
    candidates = {'Alice': 0, 'Bob': 0, 'Charlie': 0}
    voters = set()  # to track who has voted
    admin_password = "admin123"  # predefined password for admin access
    
    while True:
        print("\n1. Vote")
        print("2. View results (Admin only)")
        print("3. Reset votes (Admin only)")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ").strip()
        
        if choice == '1':
            vote(candidates, voters)
        elif choice == '2':
            view_results(candidates, admin_password)
        elif choice == '3':
            reset_votes(candidates, voters, admin_password)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
