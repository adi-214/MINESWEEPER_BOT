import os
import discord
import random

my_secret = os.environ['token']

valid_responses = [[3, 4, 5, 6, 7, 8, 9, 10], ["easy", "medium", "hard"]]

error_message = "Please enter in the following format \nmine <grid_size> <difficulty>\nGrid size must be greater than or equal to 3\nValid difficulty level are <easy> / <medium> / <hard>"

safe_count = 0
safe_guessed = 0

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    current_player = message.author
    if message.author == client.user:
        return
    if message.content.startswith('mine'):
        current_message = message.content.split()
        if (len(current_message)<3):
          await message.channel.send(error_message)
        elif ((int(current_message[1]) not in valid_responses[0]) or (current_message[2] not in valid_responses[1])):
            await message.channel.send(error_message)
        else:
            await message.channel.send("correct command to start playing")
            on_message(message)
          
              



client.run(my_secret)
