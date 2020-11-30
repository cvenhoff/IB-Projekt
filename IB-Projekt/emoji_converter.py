import userdata

def get_emoji_text(index):
    return ":"+str(list(userdata.emojis.items())[index][0])+":"
    
def text_to_emoji(content):
    content = content.split(":")
    for word in content:
        if(word in userdata.emojis.keys()):
            content[content.index(word)] = userdata.emojis[word]
    return "".join(content)
    
def emoji_to_text(content):
    res = []
    for symbol in content:
        if(symbol in userdata.emojis.values()):
            keys = list(userdata.emojis.keys())
            index = list(userdata.emojis.values()).index(symbol)
            res.append(keys[index])
        else:
            res.append(symbol)
    return "".join(res)
     