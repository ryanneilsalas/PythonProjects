# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",   
# }

# # print(programming_dictionary["Bug"])

# # #Adding new items to the dictionary
# # programming_dictionary["Loop"] = "The action of doing something over and over again."
# # print(programming_dictionary)

# # #Create and existing dictionary
# # empty_dictionary = {}

# # #wipe an existing dictionary
# # programming_dictionary = {}

# #Edit an item in a dictionary
# programming_dictionary ["Bug"]= "change something here"

# #Loop through a dictionary
# for key in programming_dictionary: 
#     print(key)
#     print(programming_dictionary[key])

# #Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# #Nesting a List in a Dictionary

# travel_log = {
#     "France" : {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits":12},
#     "Germany" : {"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visits":14},            
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

print("Welcome  to the  secret auction program.")
end_bid = False
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner=""
   
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner of the auction is {winner} with the amount of ${highest_bid}")
    
        
while not end_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your  bid?: $"))
    more_bid = input("Are there any other bidders? Type 'yes' or 'no'.  ")
    bids [name] = bid
   
    
    if more_bid == "yes" :  
    
      print("Add more bid \n")
    elif more_bid == "no":
     end_bid =True  
     find_highest_bidder(bids)
        
   
    else: 
        print("Please make a valid response")
