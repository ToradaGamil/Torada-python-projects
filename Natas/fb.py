import fbchat
import time
from fbchat import *
from fbchat.models import *
username = str(input("enter th email or user or phone or id asshole"))
password = str(input("enter the password"))
tor = Client('GTorada1', '0/0/0/',)
users = tor.fetchAllUsers()
c=0
#print("users' names: {}".format([user.name for user in users]))
#print("users' IDs: {}".format([user.uid for user in users]))

pageuser = ('635192296971587')
print("users' names: {}".format([user for user in pageuser]))

if not tor.isLoggedIn():
    tor = Client('GTorada1', '0/0/0/')
#for user in users:
    #tor.send(Message(text=user.name + 'test ess'), thread_id=user.uid, thread_type=ThreadType.USER)
    #time.sleep(1)
# client.send(fbchat.models.Message,.uid)
