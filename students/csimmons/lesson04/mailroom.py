#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons
# Edited 12/3/2020 - csimmons

import sys
from operator import itemgetter

donorlist = dict([
    ('Mary Newcomer', [10000, 2500, 300]),
    ('Christine Rutolo', [3000, 6000, 750, 20000]),
    ('Martin Acevedo', [2000, 5000]),
    ('Sutton Keaney', [24500, 500, 3000, 5000, 1000]),
    ('David Basilio', [750, 750, 750, 750, 5000, 750, 750]),
    ('Andrew Laughlin', [2500, 500, 40000, 50]),
    ('Hussein Saffouri', [1000, 1000, 2100, 7000, 55000]),
    ])

menu_prompt = '\n'.join(('Please choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Quit',
          '>>> '))

thanks_prompt = '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '\n>>>  '))

gift_prompt = '\n'.join(('\nPlease enter the donation amount ("$" and commas are not needed)',
                '>>>  '))

def print_donors(donors):
    print('\nMaster List of Donors:\n')
    for donor in donors:
        print(donor)
    print('\n')

def exist_donor(response, donors):
    gift = input(gift_prompt)   
    f_gift = float(gift)
    f_response = response.title()
    for i in range(len(donorlist)):
        if f_response == donorlist[i][0]:
            donorlist[i][1].append(f_gift)
    generate_thankyou(f_response, f_gift)

def new_donor(response):    
    f_response = response.title()
    print(('\n{} is a new donor!').format(f_response))
    gift = input(gift_prompt)
    f_gift = float(gift)
    new_donor = tuple([f_response,[ ]])
    donorlist.append(new_donor)
    get_length = len(donorlist)-1
    donorlist[get_length][1].append(f_gift)
    generate_thankyou(f_response, f_gift)

def print_donorlist(all_info):
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 32) +'\n'
    info_row = '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format
    print(header1)
    print(header2)
    for i in range(len(all_info)):
        print(info_row(dname=all_info[i][0], total=all_info[i][1], gifts=all_info[i][2], avg=all_info[i][3]))
    print('\n')

def generate_thankyou(f_response, f_gift):
    print("""\n
    Dear {},
    We would like to thank you for your extremely generous donation 
    of ${:,.2f} to the Anonymous Charity of Seattle.\n
    Sincerely,
    CA Simmons \n""".format(f_response, f_gift))

def send_thankyou(donorlist):
    donors = list(map(lambda x:x[0], donorlist))
    response = input(thanks_prompt)
    f_response = response.title()
    if response.lower() == 'list':
        print_donors(donors)
        main()
    elif response.lower() == 'exit':
        main()
    elif response.title() in donors:
        exist_donor(response, donors)
        main()
    else:
        new_donor(response)
        main()

def display_report(donorlist):
    donors = list(map(lambda x:x[0], donorlist))
    gifts = list(map(lambda x:x[1], donorlist))
    all_info = []
    for i in range(len(donorlist)):
        total_gift = 0
        average_gift = 0
        gift_info = []
        for x in range(len(gifts[i])):
            total_gift += gifts[i][x]
        average_gift = total_gift / len(gifts[i])
        gift_info.append(donors[i])
        gift_info.append(total_gift)
        gift_info.append(len(gifts[i]))
        gift_info.append(average_gift)
        all_info.append(gift_info)
    all_info = sorted(all_info, key=itemgetter (1), reverse=True)
    print_donorlist(all_info)
    main()

def main():
    response = input(menu_prompt)
    while(True):
        if response == '1':
            send_thankyou(donorlist)
        elif response == '2':
            display_report(donorlist)
        elif response == '3':
            print('\nThank You. Exiting the Mailroom Application\n')
            sys.exit()
        else:
            print('\nSorry, your response was not a valid option')
            main()

if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!')
    main()
