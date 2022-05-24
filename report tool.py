import requests




token = input("token:")

def auth(token):
  userdata = requests.get("https://discord.com/api/v9/users/@me", headers={"authorization": token}).json()
  print("{userdata['username']}#{userdata['discriminator']}")
  if userdata.status_code == 200:
    for i in range(99999):
      requests.get("https://discord.com/api/v8/users/@me/channels",headers={"authorization": token},data={"recipients": "12345678910"})
auth(token)

