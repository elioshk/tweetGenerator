# tweetGenerator

This is a project I'm working on to generate a fake tweet using any twitter account's previous tweets as the source text.
I'm using the python markovchain and snscrape packages for most of the work, and just putting them together.

The program only pulls from a maximum of 500 tweets, as scraping too many takes a very long time.

So far there is only very basic functionality, as I need to clean up the data before actually using it. Here is what a 
basic usage of it looks like right now:

generateTweet("jack") #being the account of the twitter CEO

text generated:

"Co/eqkqlt8xmc'b'b'@signalapp amazing!"

As you can see, it's picking up a lot of garbage in the file and using them as markov states.

I'll do my best to fix this. I may also remove username mentions, as they are most likely to be the states with the fewest
connections.
