import userdata
import os

def get_data():
    with open(file=os.path.join(os.path.join(os.path.dirname(__file__)), "userdata.txt"), mode="r") as file:
        content = file.read().split("\n")
    if(len(content) > 2):
        userdata.hashtags = content[0].split("~")
        userdata.hashtags = [e for e in userdata.hashtags if e != ""]
        userdata.comments = content[1].split("~")
        userdata.comments = [e for e in userdata.comments if e != ""]
        userdata.direct_messages = content[2].split("~")
        userdata.direct_messages = [e for e in userdata.direct_messages if e != ""]
    else:
        userdata.hashtags = []
        userdata.comments = []
        userdata.direct_messages = []

def set_data(list):
    content = "\n".join(list)
    with open(file=os.path.join(os.path.join(os.path.dirname(__file__)), "userdata.txt"), mode="w") as file:
        file.write(content)