import requests





def auth():
  userdata = requests.get("https://discord.com/api/9/users/@me", headers={"authorization": token}).json()
  print("{userdata['username']}#{userdata['discriminator']}")
  if userdata.status_code == 200:
    for i in range(99999):

      requests.get("https://discord.com/api/9/users/@me",headers={"authorization": token})


