import math

# Function to get the total number of hot dogs needed
def get_total_hot_dogs():
    # Input: Get the number of people and hot dogs per person
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    
    # Calculate the total number of hot dogs needed
    total = people * hot_dogs
    return total

# Function to show the results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # Output: Display the results
    print(f"Minimum packages of hot dogs needed: {min_dogs}")
    print(f"Minimum packages of hot dog buns needed: {min_buns}")
    print(f"Hot dogs left over: {dogs_left}")
    print(f"Hot dog buns left over: {buns_left}")

# Main module
def main():
    # Constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package
    
    # Step 1: Get the total number of hot dogs needed
    total_hot_dogs = get_total_hot_dogs()
    
    # Step 2: Calculate the number of leftover hot dogs and buns
    dogs_left = total_hot_dogs % DOGS  # Leftover hot dogs
    buns_left = total_hot_dogs % BUNS  # Leftover hot dog buns
    
    # Step 3: Calculate the minimum number of packages needed
    min_dogs = math.ceil(total_hot_dogs / DOGS)  # Minimum packages of hot dogs
    min_buns = math.ceil(total_hot_dogs / BUNS)  # Minimum packages of buns
    
    # Step 4: Show the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# Call the main function
if __name__ == "__main__":
    main()
