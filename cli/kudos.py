#!/usr/bin/python

import datetime
import github
import getpass
import json


icon_list = [
    # Trophy
    'https://assets-cdn.github.com/images/icons/emoji/unicode/1f3c6.png',
    # Heart
    'https://assets-cdn.github.com/images/icons/emoji/unicode/2764.png',
    # Thumbs Up
    'https://assets-cdn.github.com/images/icons/emoji/unicode/1f44d.png',
    # Tada
    'https://assets-cdn.github.com/images/icons/emoji/unicode/1f389.png',
]

authed = False
while not authed:
    user = raw_input('Your GitHub user ID: ')
    password = getpass.getpass("%s's password: " % user)

    try:
        gh = github.Github(user, password)
        name = gh.get_user().name
        authed = True
    except github.BadCredentialsException:
        print('Invalid user ID or password')
    except github.GithubException:
        print('Exception authenticating to GitHub')

user_found = False
while not user_found:
    try:
        recipient_id = raw_input('GitHub user ID of the recipient: ')
        recipient_user = gh.get_user(recipient_id)
        user_found = True
    except github.UnknownObjectException:
        print('Unknown user ID: %s' % recipient_id)

print('[1] Trophy')
print('[2] Heart')
print('[3] Thumbs Up')
print('[4] Ta-da')

icon_id = 0
while icon_id not in range(1, 5):
    try:
        icon_id = int(raw_input('Choose an icon number from 1 to 4: '))
    except ValueError:
        pass

message = raw_input('Enter your appreciation message: ')
date = datetime.datetime.now()
formatted_date = date.strftime("%a %b %d %H:%M:%S %Z %Y")

result = {
    'Icon': icon_list[icon_id - 1],
    'Date': formatted_date,
    'Name': recipient_user.name,
    'GithubID': recipient_id,
    'Message': message,
}

print(json.dumps(result))
