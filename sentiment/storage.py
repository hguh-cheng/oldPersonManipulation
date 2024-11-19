# storage.py
import sqlite3
import logging
from helpers import clean_text, get_sentiment_textblob, get_sentiment_vader

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_db(db_name='tweets.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tweets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            tweet TEXT,
            cleaned_text TEXT,
            sentiment_textblob REAL,
            sentiment_vader REAL
        )
    ''')
    conn.commit()
    conn.close()
    logging.info("Database initialized.")

def save_tweets(topic, tweets, db_name='tweets.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for tweet in tweets:
        cleaned = clean_text(tweet)
        sentiment_tb = get_sentiment_textblob(cleaned)
        sentiment_vd = get_sentiment_vader(cleaned)
        cursor.execute('''
            INSERT INTO tweets (topic, tweet, cleaned_text, sentiment_textblob, sentiment_vader)
            VALUES (?, ?, ?, ?, ?)
        ''', (topic, tweet, cleaned, sentiment_tb, sentiment_vd))
    conn.commit()
    conn.close()
    logging.info(f"Saved {len(tweets)} tweets for topic: {topic}")

def fetch_data_for_topic(topic, db_name='tweets.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT cleaned_text, sentiment_textblob, sentiment_vader
        FROM tweets
        WHERE topic = ?
    ''', (topic,))
    rows = cursor.fetchall()
    conn.close()
    return rows
