#!/usr/bin/env python3
# Title: Mailroom Part 4 (Lesson 6)
# Dev: Roslyn Melookaran
# Date: 10/28/20
# Change Log: (Who, When, What)
# R. Melookaran, 10/28/20, created script)
# --------------------------------------------------------------


# ----------Functions----------#


def options_menu():
    """ Show menu of options to user.
            :return: nothing
            """
    print("\nMenu of actions:" + '\n \t1) Send a Thank You \n \t2) Create a report \n \t3) Create Thank You files for all donors \n \t4) Quit\n')
    return


def option_input():
    """ Gather input from user on what action they want.
                :return: user_selection (string)
                """
    while True:
        user_selection = input('Please select option 1-3: ')
        try:
            user_selection = int(user_selection)
            break
        except ValueError:
            print("You must enter a number from 1-4")
    return user_selection


def person_input():
    user_input = input(
        'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
    user_input = user_input.title()
    return user_input


def donation_input():
    try:
        donation_amt = float(input("Please enter the donation amount: "))
    except ValueError:
        print("Your input was not valid!")
        donation_amt = float(input("Please enter the donation amount: "))
    return donation_amt


def thank_you_note(donor_all):
    """ User will be prompted for a Full Name.
            -If the user type list show them a list of the donor names and re-prompt.
            -If the user types a name not in the list, it will be added to data structure and used
            -If the user types a name in the list, it is used.
        -Once a name has been selected, user will be prompted for a donation amount to be added to donation history
        -Thank you note will be generated
                  :param: donor_all (dictionary of donors)
                  :return: donor_all (dictionary of donors)
                  """
    donation_new = []
    user_input = person_input()
    existing = False

    while user_input == "List":
        for k, v in donor_all.items():
            print("%s has made the following donations: %s" % (k, v))
        user_input = person_input()
    donation_amt = donation_input()
    donation_new = [user_input, donation_amt]

    for k, v in donor_all.items():
        if donation_new[0] == k:
            v.append(donation_new[1])
            existing = True
    if existing != True:
        donor_all.update({donation_new[0]: [donation_new[1]]})
    print("The following thank you note will be emailed to the donor: ")
    print(
        '"Dear {}, \n Thank you so much for your gracious donation of ${:.2f}. We are so thankful for your strong support!! \nCheers,\nRoslyn Melookaran"'.format(
            donation_new[0], donation_new[1]))
    return donor_all


def create_report(donor_all):
    """ Create a report of donors to show user.
                :param: donor_all (list of list)
                :return: nothing
                """
    sorted_donors = sorted(
        ([sum(value), key, len(value), (sum(value) / len(value))] for key, value in donor_all.items()), reverse=True)
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f'{title[0]:20}|{title[1]:^12}|{title[2]:^10}|{title[3]:^14}|')
    print("-" * 60)
    for person in sorted_donors:
        print(f'{person[1]:20}  ${person[0]:^12}{person[2]:9}      ${person[3]:^12}')
    print("\n")
    return sorted_donors


def send_all_thank_you(donor_all):
    """ Function will print a .txt file thank you note for each donor in list
            :param: donor_all (list of lists)
            :return: nothing
            """
    for k, v in donor_all.items():
        tot = sum(v)
        string = "Dear %s, \n\n \t Thank you so much for your support! You have donated a total of $%s, which is so very appreciated. We hope to have your continued support through these times. \n\nThanks, \nRoslyn" % (k, tot)
        filename = k
        filename = filename.replace(" ", "")
        filename = filename + ".txt"
        with open(filename, 'w') as f:
            f.write(string)
        print("Thank you note files have been created and saved in current folder!")
    return


# ----------Variables----------#
donor_dict = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00], 'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00]}
user_input = ""
dict = {
    1: thank_you_note,
    2: create_report,
    3: send_all_thank_you
}

# ----------Main----------#
if __name__ == '__main__':
    options_menu()
    user_input = option_input()
    while user_input != 4:
        dict.get(user_input)(donor_dict)
        options_menu()
        user_input = option_input()
    exit_input = input('Thanks for using the program. Hit enter to exit.')