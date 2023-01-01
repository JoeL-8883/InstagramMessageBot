import bot

# Login
while True:
    try:
        input_username = input("Enter username: ")
        input_password = input("Enter password:")
        instagram_bot = bot.Bot(input_username, input_password)
        instagram_bot.login()
        exit
    except:
        print("Incorrect login details")

# Specify users
recipients = {
    "username1":"forename1",
    "username2":"forename2"
}
    
# Specify message
input_message = "Happy new year "

for username in recipients:
    forename = recipients[username]
    instagram_bot.message(username, message + forename + "!") 


