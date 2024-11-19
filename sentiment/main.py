# main.py
import time
import random
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from helpers import get_browser, human_delay
from storage import init_db, save_tweets, fetch_data_for_topic
from dotenv import load_dotenv
import os
import schedule

# Load environment variables
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TwitterSentimentAnalyzer:
    def __init__(self, username, password, db_name='tweets.db'):
        self.username = username
        self.password = password
        self.db_name = db_name
        self.driver = get_browser(headless=True)
    
    def login(self):
        logging.info("Navigating to Twitter login page.")
        self.driver.get("https://twitter.com/login")
        human_delay(3,5)  # Wait for page to load

        try:
            username_input = self.driver.find_element(By.NAME, "session[username_or_email]")
            password_input = self.driver.find_element(By.NAME, "session[password]")
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            password_input.submit()
            logging.info("Submitted login form.")
            human_delay(5,7)  # Wait for login to process
        except NoSuchElementException as e:
            logging.error("Login elements not found.")
            self.driver.quit()
            raise e

    def navigate_to_trending(self):
        logging.info("Navigating to Twitter trending page.")
        self.driver.get("https://twitter.com/explore/tabs/trending")
        human_delay(3,5)

    def get_trending_topics(self):
        logging.info("Fetching trending topics.")
        trending = []
        try:
            topics = self.driver.find_elements(By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')
            for topic in topics:
                text = topic.text
                if text and text not in trending:
                    trending.append(text)
            logging.info(f"Found {len(trending)} trending topics.")
        except Exception as e:
            logging.error("Error fetching trending topics.")
        return trending

    def get_tweets_for_topic(self, topic, max_tweets=100):
        logging.info(f"Fetching tweets for topic: {topic}")
        search_url = f"https://twitter.com/search?q={topic}&src=trend_click&f=live"
        self.driver.get(search_url)
        human_delay(3,5)
        tweets = []
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while len(tweets) < max_tweets:
            page_tweets = self.driver.find_elements(By.XPATH, '//article[@role="article"]//div[@lang]')
            for tweet in page_tweets:
                try:
                    text = tweet.text
                    if text and text not in tweets:
                        tweets.append(text)
                        if len(tweets) >= max_tweets:
                            break
                except Exception:
                    continue
            # Scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            human_delay(2,4)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                logging.info("No more tweets found.")
                break
            last_height = new_height
        logging.info(f"Collected {len(tweets)} tweets for topic: {topic}")
        return tweets[:max_tweets]

    def collect_and_store(self):
        try:
            self.login()
            self.navigate_to_trending()
            trending_topics = self.get_trending_topics()
            for topic in trending_topics:
                tweets = self.get_tweets_for_topic(topic, max_tweets=100)
                save_tweets(topic, tweets, db_name=self.db_name)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            self.driver.quit()
            logging.info("Browser closed.")

def job():
    logging.info("Starting tweet collection job.")
    analyzer = TwitterSentimentAnalyzer(
        username=os.getenv("TWITTER_USERNAME"),
        password=os.getenv("TWITTER_PASSWORD")
    )
    analyzer.collect_and_store()
    logging.info("Tweet collection job completed.")

def start_scheduler():
    schedule.every().hour.do(job)  # Schedule to run every hour
    logging.info("Scheduler started. Running tweet collection every hour.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Initialize the database
    init_db()
    # Start the scheduler
    start_scheduler()
