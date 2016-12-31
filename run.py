#!/usr/bin/python
import argparse

import discord
import asyncio

# Fun imports
from fun.quote import print_quote
from fun.response import *

# Development Constants
DEV_BOT_NAME = "Harambot-Dev"
DEV_BOT_KEY = "MjQ5NTkwMTE3MzU2Nzk3OTUz.CxIg5A.BYYtQ1H4H3l4CuLl-YrWjI50eOk"

# Production Constants
PRODUCTION_BOT_NAME = "Harambot 🍌"
PRODUCTION_BOT_KEY = "MjQ2MTMxMjkyMjg5MjM2OTky.CxIzbg.ftm3bhYcnsceIm2bgLQDlx7UmOk"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): # placeholder "bookmarks"
    # also we want to post messages in the channe lwhere the user asked, but
    # if possible make the message only viewable to them kinda like the default bot can do
    if message.author.name == DEV_BOT_NAME or message.author.name == PRODUCTION_BOT_NAME:
        pass
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, 'I\'m a fuckboy.')
    # fun stuff
    elif message.content.lower().startswith('!chuckquote'):
        await print_quote(client, message, "chuck")
    elif message.content.lower().startswith('!peterquote') or message.content.lower().startswith('!petequote'):
        await print_quote(client, message, "peter")
    elif "banana" in message.content.lower():
        await client.send_message(message.channel, SHOCKED_MONKEY_URL + "\n... I love bananas. + 100 EP")
    elif "joke" in message.content.lower():
        await tell_joke(client, message)
    elif "love" in message.content.lower() and "harambot" in message.content.lower():
        await client.send_message(message.channel, "\n:monkey_face: + 50 EP I love you too, " + message.author.name + ". :monkey_face:\n" + LOVE_GORILLA_URL)
    elif "fuck" in message.content.lower() and "harambot" in message.content.lower():
        await client.send_message(message.channel, MIDDLE_FINGER_GORILLA_URL + "\n:monkey: - 50 EP :monkey:")
    elif "harambot" in message.content.lower() and is_message_a_greeting(message):
        await client.send_message(message.channel, ":banana: :monkey_face: Greetings, " + message.author.name + ". :banana:")
    elif "harambot" in message.content.lower() and is_message_a_thank_you(message):
        await client.send_message(message.channel, ":banana: :monkey_face: You got it, " + message.author.name + ". :banana:\n" + NO_PROBLEM_GORILLA)
    elif did_mention_harambot(client, message):
        await client.send_message(message.channel, ":monkey: You rang, " + message.author.name + "? :monkey:")
    elif "harambot" in message.content.lower():
        await client.send_message(message.channel, "Someone called?")

if __name__ == "__main__":
    '''
    Add two mutually exclusive commands, where one of the two is required for the
    script to run.
    '''
    parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d','--dev',help="Run the bot in development mode.",action="store_true")
    group.add_argument('-p', '--prod',help="Run the bot in production mode.",action="store_true")
    args = parser.parse_args()

    client.accept_invite('https://discord.gg/mM5fXCe')

    if args.dev:
        client.run(DEV_BOT_KEY)
    elif args.prod:
        client.run(PRODUCTION_BOT_KEY)
    else:
        print("RIP in peace.")
