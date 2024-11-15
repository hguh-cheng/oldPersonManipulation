### Article Display

**Priority:** [P0]
**Implementation Timeline:** [Day 1-2]

**Core Requirements:**

- Working home page with functionality for articles, headlines
- Allow user to click on articles via other articles

**Technical Components:**

- ReactJs
- HTML

**Simplifications:**

- At this stage, home page does not need to be personalized

### User Account Setup

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

## Day 1-2 (Core Framework)

- Make home page with clickable articles

## Day 2-4 (User Setup)

- Allow users to create accounts, have profiles, and if possible, track their engagement data on the site

## Day 3-5 (Tailoring/Enhancement)

Do whichever time permits:

- Option 1: Use engagement data to tailor articles for the user
- Option 2: Give the user many easier personalization features, including daily streak, badges/achievements, notifications, dark mode, etc.
- Test website functionality
