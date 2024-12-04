### Twitter scraping (TO DO)
**Priority:** [P0]
**Implementation Timeline:** [Day 1-2]

**Core Requirements:**

- Log into twitter, scrape the trending topics into csv file, then scrape some amount (I was thinking 200) of tweets from each trending topic organize into db

**Technical Components:**

- Python
- Playwright
- MongoDB
- CSV


**Simplifications:**

- Ignore multimedia, only scrape text and emojis
- Can ignore the metrics of the tweets (likes, shares, retweets, ect.)

**Current State**
- It logs into twitter with .env data and scrapes the topics from the trending news page with decent logging and screenshots for each steps

**To Do**
- You should create new methods in the scrape.py file and reference them in the combined.py file. Make sure you aren't creating a new browser instance (This messes up the cookies)
- Go to the trend links from the trends.csv file and scrape ~200 tweets from each trending topic into a MongoDB database
- You must find the stable atributes for tweets and containers. This involves going to the trending news page on twitter, inspecting the page, and giving ChatGPT the sections of html 
- You cannot just give it the whole webpage but I would copy the entire container it is in as well as a single post inside the container so it knows what to look for
- I reccomend taking perodic screenshots to know it's on the right page or scrolling properly or you could turn off headless mode (this will have a real browser pop up and you can watch it. Playwright is super fineky though so this could take the whole class to figure out)



### Sentiment analysis

**Priority:** [P0]
**Implementation Timeline:** [Day 1-2]

**Core Requirements:**

- Only after the data is scraped from twitter, analyze with VADER making sure to include emojis
- This should get a general sentiment score for each trend and indentify key words apart from the trend's title

**Technical Components:**

- Python
- VADER / nltk (Python libraries for sentiment analysis)
- MongoDB


**Simplifications:**

- Ignore multimedia, only scrape text and emojis
- Can ignore the metrics of the tweets (likes, shares, retweets, ect.)


### Article Display 

**Priority:** [P2]
**Implementation Timeline:** [Day 1-2]

**Core Requirements:**

- Working home page with functionality for articles, headlines
- Allow user to click on articles via other articles

**Technical Components:**

- HTML
- CSS

**Simplifications:**

- At this stage, home page does not need to be personalized

### User Account Setup 
### Completed first steps no database

**Priority:** [P1]
**Implementation Timeline:** [Day 2-4]

**Core Requirements:**

- Allow user to create account with username/password
- Basic profile interface with some user stats
- If possible, record user data for tailoring algorithm

**Technical Components:**

- MongoDB
- Firebase Authentication

**Simplifications:**

- At minimum, just have a profile

**Dependencies:**

- Working home page with articles to click on

### Personalization of Articles

**Priority:** [P2]
**Implementation Timeline:** [Day 3-5]

**Core Requirements:**

- Interpret user history and feed them similar articles
- Basic profile interface with some user stats

**Technical Components:**

- Python code to do sentiment analysis based on user experience with other articles
- Access to user history

**Simplifications:**

- User metrics can just include articles clicked on (rather than tracking time spent on each article, likes/comments etc.)

**Dependencies:**

- Requires implementation of user data collection

# MVP Implementation Plan

## Day 1-2 (Core Framework) Done for now

- Make home page with clickable articles

## Day 2-4 (User Setup) Done for now

- Allow users to create accounts, have profiles, and if possible, track their engagement data on the site

## Day 3-5 (Article creation)

- Scrape data from twitter with Playwright and analyze sentiment with VADER
