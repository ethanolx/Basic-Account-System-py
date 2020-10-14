# Points and Accounts Management System(PAMS) for campaign USE_LESS

# Reset system
accounts = [0]
pw_mng_syst = {}
pt_mng_syst = {}

# Settings
conversion_rate = 1000 # in points per dollar(decimal)

while True:
    print("\nActions:\n1) Create new account\n2) Open existing account\n")
    print("What do you wish to do?")
    try:
        action = int(input(">"))
        if action == 1:
            print("Please set a valid password for your account")
            password = input("Password: ").strip()
            confirm_password = input("Confirm password: ").strip()
            if password == confirm_password:
                accounts.append(int(accounts[-1]) + 1)
                pw_mng_syst[accounts[-1]] = password
                pt_mng_syst[accounts[-1]] = 0
                print("Your account number is " + str(accounts[-1]))
            else:
                print("Your passwords do not match!")
        elif action == 2:
            print("Please enter your account number in the space below:")
            try:
                account = int(input("Account number: "))
                if account in accounts:
                    print("Please enter your password")
                    pw = input("Password: ")
                    if pw == pw_mng_syst.get(account):
                        print("Your password is correct")
                        points = pt_mng_syst.get(account)
                        print("\nActions:\n1) Add points\n2) Redeem points\n3) Check points balance")
                        sub_action = int(input(">").strip().lower())
                        if sub_action == 1:
                            print("How much?")
                            amount_to_add = int(input(">"))
                            pt_mng_syst[account] = points + amount_to_add
                        elif sub_action == 2:
                            print(f"Your points({points}) amount to ${points/conversion_rate}")
                            print("How much do you want to redeem?")
                            amount_to_redeem = float(input("$"))
                            if amount_to_redeem > (points/conversion_rate):
                                print("You do not have sufficient points to redeem $" + str(amount_to_redeem) + "!")
                            elif amount_to_redeem < 0:
                                print("You cannot redeem this negative amount!")
                            else:
                                pt_mng_syst[account] = points - (amount_to_redeem * conversion_rate)
                        elif sub_action == 3:
                            print(f"You have {points} points/${points/conversion_rate} left")
                    else:
                        print("Your password is wrong")
                else:
                    print("Please enter a valid account number!")
            except NameError:
                print("Invalid input!")
            except ValueError:
                print("Invalid input!")
        elif action == 3:
            print(accounts)
        else:
            print(":)")
            break
    except NameError:
        print("Invalid input!")
    except ValueError:
        print("Invalid input!")
