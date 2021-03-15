# Stewie is insulting you bot
Oh, I offended you with my opinion? You should hear the ones I kept to myself.
Sure you like that this little bastard that Stewie Griffin is insults you. So this bot is about that. It will deploy a pic of Stewie insulting you, or maybe take this idea to insult another person. [Samu](https://twitter.com/stewieisangry)<br>

## What it is?
This is a twitter bot that tweets daily one sarcastic insult but put in a pic of Stewie Griffin. It is automated with **Python** and a **Lambda Function** in **AWS**. 

I based this project, twitching and modifying it here and there, on [@_dylancastillo](https://twitter.com/_dylancastillo)'s bot, who wrote an excellent [template](https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda) and a great [tutorial](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/) accompanying it. **All credit goes to him.**
But i will thanks also [DavidCarricondo](https://github.com/DavidCarricondo) to lend me a hand and hear me when nothing goes well.

## How it works?

+ First, there is a very basic web scrapping from a [plain static web](https://parade.com/1079501/stephanieosmanski/sarcastic-quotes/) containing the desired messages to post. To ease use it and create a csv file with it i used [import_quotes.py](https://github.com/raistln/Twitter_bot_lambda_version/blob/master/src/import_quotes.py), where is the code to clean with a little bit of regex the scraped quotes.

+ The main functions that retrieve the tweets and post them using the Twitter API are in [lambda_function.py](https://github.com/raistln/Twitter_bot_lambda_version/blob/master/src/lambda_function.py).

+ The [createlambdalayer.sh](https://github.com/raistln/Twitter_bot_lambda_version/blob/master/createlambdalayer.sh) creates a lambda layer with the libraries in requirements.txt and using a **Docker image**. This is the layer that will be uploaded to AWS.

+ The [buildpackage.sh](https://github.com/raistln/Twitter_bot_lambda_version/blob/master/buildpackage.sh) only wraps the function in a zip file to upload it as a lambda function. 

+ The lambda function is scheduled using **EventBridge**

