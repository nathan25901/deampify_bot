# https://www.google.com/amp/www.example.com/amp.doc.html

import praw
import os
import logging

logging.basicConfig(level=logging.INFO)
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("testingground4bots")


def main():
    for submission in subreddit.hot(limit=2):
        comment_list = []
        try:
            for top_level_comment in submission.comments:
                logging.info("L1: " + top_level_comment.body)
                comment_list.append(top_level_comment)

                for second_level_comment in top_level_comment.replies:
                    logging.info("\tL2: " + second_level_comment.body)
                    comment_list.append(second_level_comment)

                    for third_level_comment in second_level_comment.replies:
                        logging.info("\t\tL3: " + second_level_comment.body)
                        comment_list.append(third_level_comment)

                        for fourth_level_comment in third_level_comment.replies:
                            logging.info("\t\t\tL4: " + third_level_comment.body)
                            comment_list.append(fourth_level_comment)

                            for fifth_level_comment in fourth_level_comment.replies:
                                logging.info("\t\t\t\tL5: " + fourth_level_comment.body)
                                comment_list.append(fifth_level_comment)

            process_comment(comment_list)
                # body = top_level_comment.body
                # if ("https://www.google.com/amp/") in body:
                #     no_amp_body = body.replace("https://www.google.com/amp/", "")
                #     top_level_comment.reply(no_amp_body)
        except AttributeError:
            pass


def process_comment(comment_list):
    for comment in comment_list:
        body = comment.body
        if ("https://www.google.com/amp/") in body:
            no_amp_body = body.replace("https://www.google.com/amp/", "")
            comment.reply(no_amp_body)
            logging.info(body + " replaced with: " + no_amp_body)

main()

# for comment in subreddit.stream.comments(limit=5):
#     if "amp" in comment.body:
#         comment.reply("Hello!")
#
# if not os.path.isfile("posts_replied_to.txt"):
#     f = open("posts_replied_to.txt", "w")
#     # posts_replied_to = []
# else:
#     with open("posts_replied_to.txt", "r") as f:
#         posts_replied_to = f.read()
#         posts_replied_to = posts_replied_to.split("\n")
# #         posts_replied_to = list(filter(None, posts_replied_to))




