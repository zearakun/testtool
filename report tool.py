import requests




token = input("token:")
guild = input("guild:")
channel = input("channel")
message = input("message:")
def auth(token):
  userdata = requests.get("https://discord.com/api/9/users/@me", headers={"authorization": token}).json()
  print("{userdata['username']}#{userdata['discriminator']}")
  if userdata.status_code == 200:
    for i in range(99999):

      requests.get("https://discord.com/api/9/users/@me",headers={"authorization": token})
auth(token)

