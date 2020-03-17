import auth
from record import getRecord

import praw
import re

# Get our api access tool
# Note: this data is not in the github for security reasons
reddit = praw.Reddit(client_id=auth.client_id, client_secret=auth.client_secret, user_agent=auth.user_agent, username=auth.username, password=auth.password)

print('Running as: ' + str(reddit.user.me()))

def getResponce(command):
    chunks = command.split(" ")
    if len(chunks) == 1:
        chunks.append("all")
    return getRecord(chunks[1]) + "\n\n[source code](https://github.com/m-leila/biden_bot) - [issues](https://github.com/m-leila/biden_bot/issues/new)"

if __name__ == "__main__":
    command_re = re.compile(r"u/biden_bot( \S+){,1}")
    for comment in reddit.subreddit('test').stream.comments():
        command = command_re.search(comment.body)
        if command != None and not comment.saved and comment.author != reddit.user.me():
            comment.save()
            comment.reply(getResponce(command.group(0)))
