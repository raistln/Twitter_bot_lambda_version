import os
import random
import json
from pathlib import Path
import tweepy
import csv
from PIL import Image, ImageFont, ImageDraw 
import re

ROOT = Path(__file__).resolve().parents[0]

def stewies_angry(tweets_file):
    
    pics_ = os.listdir(ROOT / "stewie_pics/")
    picture = random.choice(pics_)
    my_image = Image.open(ROOT / "stewie_pics" / picture)
    max_size = (530,530)
    my_image.thumbnail(max_size)
    title_font = ImageFont.truetype(str(ROOT.joinpath("Roboto_Bold.ttf")), 18)
    
    with open(ROOT / "stewie_angry.csv", newline='') as quote:
        reader = csv.reader(quote)
        angry = list(reader)
    with open(ROOT / "excluded.csv", newline='') as quote:
        reader = csv.reader(quote)
        excluded = list(reader)
    
    insults = [insult for insult in angry if insult not in excluded]
    choosed = random.choice(insults)

    with open(ROOT / "excluded.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(choosed)
    
    quote = re.split(r"\.|\,", choosed[0], 1)
    
    if len(quote) == 2:
        title_text1 = quote[0] + ","
        title_text2 = quote[1]
    else:
        splitted = quote[0].split(" ")
        title_text1 = " ".join(splitted[:len(splitted)//2])
        title_text2 = " ".join(splitted[len(splitted)//2:])
    
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((25,20), text=title_text1, fill=(40, 46, 46), font=title_font)
    image_editable.text((65,60), text=title_text2, fill=(40, 46, 46), font=title_font)
    final_pic = my_image.save(ROOT / "result.jpg")
    
    if len(excluded) == (len(angry)-5):
        with open(ROOT / "excluded.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(choosed)

def lambda_handler(event, context):
    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Get tweet from csv file")
    tweets_file = ROOT / "stewie_angry.csv"
    stewies_angry(tweets_file)
    print(f"Posting tweet")
    api.update_with_media(ROOT / "result.jpg")

    return {"statusCode": 200}
