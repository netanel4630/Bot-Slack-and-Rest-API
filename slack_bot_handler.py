from slack_bot import *
from botConfig import *
import time
import threading


def checkCommands(bot):
    while True:
        parseText(bot.slackReadRTM())
        time.sleep(CHECK_COMMANDS)

def sendTime(bot):
    while True:
        time.sleep(SEND_TIME)
        bot.writeToSlack(getTime())

def parseText(text):
    if text and len(text) > 0:
        if 'blocks' in text[0]:
            if text[0]['blocks'][0]['elements'][0]['elements'][0]['text'] == COMMAND:
                bot.writeToSlack(getTime())
            if text[0]['blocks'][0]['elements'][0]['elements'][0]['text'] == TWITTER_COMMAND:
                send_from_twitter()

def getTime():
    return time.ctime(time.time())

#TODO: get tweets from rest api and send to slack
def send_from_twitter():
    pass

if __name__ == '__main__':
    bot = slack_bot(BOT_TOKEN, CHANNEL)

#Thread for check the commands from user
    commandHandlerT = threading.Thread(target=checkCommands(bot))
    commandHandlerT.daemon = True
    commandHandlerT.start()

# Thread for send time to slack every SEND_TIME seconds
    sendTimeT = threading.Thread(target=sendTime(bot))
    sendTimeT.daemon = True
    sendTimeT.start()