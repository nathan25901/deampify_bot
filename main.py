# https://www.google.com/amp/www.example.com/amp.doc.html

import praw
import os
import logging
import datetime

logging.basicConfig(filename = 'bot.log', level=logging.INFO)
# logging.basicConfig(level=logging.INFO)

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("testingground4bots")
reference_website = f"https://www.polemicdigital.com/google-amp-go-to-hell/"


def main():

    for comment in subreddit.stream.comments():
        process_comment(comment)


def process_comment(comment):

    body = comment.body
    if "https://www.google.com/amp/" in body:
        with open("comment_log.txt", "r+") as comment_log:

            if str(comment) not in comment_log.read():
                no_amp_body = body.replace("https://www.google.com/amp/", "")
                comment.reply("Here's your link without Google AMP:\n\n" + no_amp_body + "\n\n----\n" + "[Why is Google AMP bad?](" + reference_website + ")")
                logging.info(str(datetime.datetime.now()) + "\n\t" + str(comment).strip() + "\n\t" + body + " replaced with: " + no_amp_body)
                comment_log.write("\n" + str(comment))


main()






