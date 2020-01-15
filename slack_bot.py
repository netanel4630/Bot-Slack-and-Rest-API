from slackclient import SlackClient

#class for communicate with slack bot
class slack_bot:

    def __init__(self, bot_token, channel):
        self.slack_client = SlackClient(bot_token)
        self.slack_Connect()
        self.channel = channel

    def slack_Connect(self):
        self.slack_client.rtm_connect()


    def slackReadRTM(self):
        return self.slack_client.rtm_read()

    def writeToSlack(self, text):
        return self.slack_client.api_call("chat.postMessage", channel = self.channel, text = text, as_user = True)
