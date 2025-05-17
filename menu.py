# define the menu
menu = {
    'pizza':100,
    'pasta':120,
    'burger':130,
    'coffee':110,
}

#greet
print("\t\twelcome to the cafe")
print("Cafe Policy :Maximum of 5 orders at a time to ensure quality...")
print(" Pizza: rs 100 \n pasta: rs 120 \n burger: rs 130 \n coffee: rs 110")

order_total = 0
item = []

user_reply = input("Would you like to order anything? (yes/no)\t").lower()

if user_reply == "yes":
    print("enter done once you have orderered everything")

    for i in range (5): #to allow a maxm of 5 orders

        while True: # to repeat the req for item _ till user provides something available in the menu
            current_item=input(f"Item {i+1}:\t").lower()

            if current_item in menu:
                order_total += menu[current_item]
                #opened a text file to store the users requested items
                with open("orders.txt","a") as file:
                    file.write(f"{current_item}\n")
                break
            #exit while true condition 
            elif current_item == "done":
                break
            else:
                print("We dont have this item in our menu")
        #exit for loop 
        if current_item == "done":
            break

                
 #showed the ordered items using txt file       
with open("orders.txt" , "r") as file:
    lines = file.readlines()
print("Your order is:\n")
for line in lines:
    print(line)     
print(f"Total price: {order_total}")

#deleted the txt file contents 
open("orders.txt", 'w').close()
