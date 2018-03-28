import datetime
from email.mime import text
import github
import getpass
import json
import smtplib
import sys


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


def _authenticate():
    authed = False
    while not authed:
        user = raw_input('Your GitHub user ID: ')
        password = getpass.getpass("%s's password: " % user)

        try:
            gh = github.Github(user, password)
            gh.get_user()
            authed = True
        except github.BadCredentialsException:
            print('Invalid user ID or password')
        except github.GithubException:
            print('Exception authenticating to GitHub')
    return gh


def _get_kudos(gh):
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
        'Email': recipient_user.email,
        'Message': message,
    }
    return result


def _send_email(gh, kudos, commit_id):
    authenticated = False
    while not authenticated:
        try:
            # smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_host = raw_input('Enter your SMTP Server: ')
            smtp_ssl_port = 465

            username = raw_input('Username or Email Address: ')
            password = getpass.getpass("%s's password: " % username)

            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            authenticated = True
        except smtplib.SMTPAuthenticationError:
            print('Invalid username or password')

    sender = 'NOREPLY@kudos-badges.com'
    targets = [kudos['Email']]

    message = ("""You have been sent a kudos from %s

Simply copy the following into a web page (for example your
username.github.io page) in order to display your Kudos Badge:

<script type="text/javascript"> <!--//repo="tpepper/kudos-badge";
commit="%s"; //--></script>
<script src="https://rawgit.com/tpepper/kudos-badge/master/kudo.js"><
/script>
<div id="kudo">loading...</div>
""" % (gh.get_user().name, commit_id))

    msg = text.MIMEText(message)
    msg['From'] = sender
    msg['To'] = ', '.join(targets)
    msg['Subject'] = "Congratulations you've been sent kudos!"

    server.sendmail(sender, targets, msg.as_string())
    server.quit()


def main():
    # Authenticate to GitHub
    gh = _authenticate()

    # Gather the kudos information
    kudos = _get_kudos(gh)
    # print(json.dumps(kudos))

    # Create a commit to badge repo
    # repo = gh.get_repo("tpepper/kudos-badge", lazy=True)
    # repo.create_git_commit(json.dumps(result), None, None)
    commit_id = '304df04d0ecef5452fa0ad06c3d7037ac4410c2c'

    # Send email to recipient
    _send_email(gh, kudos, commit_id)

if __name__ == '__main__':
    sys.exit(main())
