import praw
import pprint
import re

#take string and search for presence of numeral(s). returns match object
def checkForNumeral(post):
    return re.search('\d')

#searches and deletes all non-whitespace special characters
def formatPost(post):
    formatted = re.sub('[^A-Za-z0-9\s]+', '', post)
    return formatted

#searches for phone number. returns match object
def findNumber(newPost):
        #is this better?: '\d{3}\s?\d{3}\s?\d{4}'
        #this seems a little cleaner since we no longer have
        #to worry about special characters
        pattern = re.compile('^\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})$')
        numberFound = pattern.search(newPost)
        return numberFound

#deletes submission or comment
def removePost(item):
    item.delete()


def main():
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         password='',
                         user_agent='testscript.v1.0./u/freenet420',
                         username='')
    subreddit = reddit.subreddit('ZenDen').new(limit=100)


    for submission in subreddit:

        newPost = formatPost(submission.selftext)

        #I need some help getting these if statments out of main()
        if checkForNumeral():
            numberFound = findNumber(newPost)

        if numberFound:
            removePost(submission)


            #try to keep a stament like if or while or anything
            #outside of this loop
            #think of this like the main that runs little parts
            #of the program.

            #you may find that you have to use it with the way you
            #are thinknig of doing and if thats so, go for it.

main()


#Ideas:
#Use an if that checks posts for numbers in the first place that way
#we dont go over anything that doesnt have a number in itself.

#Locial Flow:
#main, formatPost, checkForNumber, findNumber, removeNumber

#Alternate Logical Flow (if there is no number in post don't format)
#main, checkForNumber, formatPost, findNumber, removeNumber
