#!/usr/bin/python
import argparse
import discord
import asyncio
import os

# Fun imports
from fun.response import *

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message): # placeholder "bookmarks"
    # Don't generate a message if it came from another bot. This may be added
    # later.
    if is_bot(message.author):
        pass
    # Easy check for if the bot is awake.
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, "I\'m awake.")
    # Respond to bananas.
    elif "banana" in message.content.lower():
        await client.send_message(message.channel, SHOCKED_MONKEY_URL + "\n... I love bananas. + 100 EP")
    # Tell jokes
    elif "joke" in message.content.lower():
        await tell_joke(client, message)
    # Respond to someone saying they love the bot.
    elif "love" in message.content.lower() and "harambot" in message.content.lower():
        await client.send_message(message.channel, "\n:monkey_face: + 50 EP I love you too, " + message.author.name + ". :monkey_face:\n" + LOVE_GORILLA_URL)
    # Respond to rudeness towards the bot.
    elif "fuck" in message.content.lower() and "harambot" in message.content.lower():
        await client.send_message(message.channel, MIDDLE_FINGER_GORILLA_URL + "\n:monkey: - 50 EP :monkey:")
    # Respond to being greeted.
    elif "harambot" in message.content.lower() and is_message_a_greeting(message):
        await client.send_message(message.channel, ":banana: :monkey_face: Greetings, " + message.author.name + ". :banana:")
    # Respond to being thanked.
    elif "harambot" in message.content.lower() and is_message_a_thank_you(message):
        await client.send_message(message.channel, ":banana: :monkey_face: You got it, " + message.author.name + ". :banana:\n" + NO_PROBLEM_GORILLA)
    # Respond to being mentioned.
    elif did_mention_harambot(client, message):
        await client.send_message(message.channel, ":monkey: You rang, " + message.author.name + "? :monkey:")
    # Amore general check for being mentioned.
    elif "harambot" in message.content.lower():
        await client.send_message(message.channel, "Someone called?")

def is_bot(member):
    return is_member_of_role(member, "botlords")

def is_member_of_role(member, role_name):
    for role in member.roles:
        if role_name == role.name:
            return True
    return False

if __name__ == "__main__":
    '''
    Add two mutually exclusive commands, where one of the two is required for the
    script to run.
    '''
    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--dev", help="Run the bot in development mode.", action="store_true")
    group.add_argument("-p", "--prod", help="Run the bot in production mode.", action="store_true")
    args = parser.parse_args()

    if args.dev:
        client.run(os.environ["FUN_BOT_DEVELOPMENT_TOKEN"])
    elif args.prod:
        client.run(os.environ["FUN_BOT_PRODUCTION_TOKEN"])
    else:
        print("Error: Bot Environment Ambiguous")
