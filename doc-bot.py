from slackclient import SlackClient
import time
import datetime
import re
 
slack_client = SlackClient("xoxb-328227269735-aLAd3oOOd7OrzHgnbZGfwyI9")

def doc_bot():
    if slack_client.rtm_connect(with_team_state=False):
        while True:
            for d in (slack_client.rtm_read()):
                if (d.get('text') != None and d.get('subtype') == None and "?" in d['text']):
                    slack_user_name = "".join(["<@", d['user'], ">"])
                    question_from_user = d['text']
                    channel_question_from = d['channel']
                    text_to_send = " ".join(["*New Help Center Message*\n", slack_user_name, "asked:", "_" + question_from_user + "_"])
                    attachment_url = "".join(["https://attentionseeking.slack.com/archives/", channel_question_from, "/", "p", d['ts']])
                    sendit = slack_client.api_call("chat.postMessage",channel="C9Q6E67L4", text=text_to_send, attachments=[{"fallback": "See","actions": [{"type": "button","text": "View Message :hash:","url": attachment_url}]}])
            time.sleep(1)
    else:
        print "Connection Failed"

doc_bot()
