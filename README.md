#  ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) New-Light Technologies: Situational Awareness for Disasters


---
**By: Victor Belei, Nathan Lee, and Jorge Ramos**


## Defining the Problem

When disaster strikes, it is critically important to provide the most relevant information to first responders and the general public. During a disaster, people are inundated with a barrage of news sources, resulting in an environment of confusing and misinformation. As of right now, there is no central medium to find relevant news sources for a disaster specific article. The goal of this project is to deliver to the public a website where users can find relevant information and get the key facts during a disaster.

---

## Executive Summary

---

### Data Collection:
In order to accomplish our goal, we needed to create a large database of articles. There were multiple options to consider in choosing the best API for our project. Some options were Google Tends, Reddit API, News API, New York Time API, and Bing API.

We ultimately chose News API because of its developer friendly qualities, and it provided the title, image, and article metadata that perfectly fit the parameters of our deliverables. However, News API does have a few weaknesses. Unless the user is willing to fork out a couple hundred dollars a month, the maximum limit of articles in a webscraping session is 500. With our three group members, that meant we could only scrape a maximum of 1500 articles every 24 hours. Even more, News API limits scraping to a one-month time period. This led us to one conclusion, we needed more articles.

Before continuing, we need take this opportunity to thank the groups before us who gathered thousands of news articles before us. We sifted through past projects and found data that fit our parameters. Two groups used News API and one group used New York Times API to scrape their data. After removing duplicates, our database contained over 10,000 articles.

---

### Data Dictionary
| Column | Description |
| --- | ---|
|Author| Author of article|
|Content | Content of article|
|Description| A short description of the article|
|Photo_url | The primary image shown in article |
|Pub_data | Date of article publication |
|Source | Publishers of the article |
|Title| title of the article |
|URL | The link to the article |
|Combined_text | A cell that combines the title, content, and description of the article|
|Tokens| The tokenized set of the combined_text column|
|Lems | The lemmatized tokens of combined_text |
|Stems| The stemmed tokens of combined_text|
|Keywords | The result of the NLTK library "Rake" that extracts keywords from combined_text|

### Model Selection:
We had a few options to attack the problem at band.
#### ![](https://cdn.baekdal.com/_img/2018/readingnews20.jpg)
**1. Sort by relevance:**
Like many of the groups before us, we would build a classification model with labeled data, and try to train a model based on the labeled data. The downside to this is that there is no obvious way to label the data relevant or irrelevant. Past groups who attempted this project spent a considerable amount of time manually labeling whether an article was relevant or not. Since we only had three people in our group, we decided this was not our best course of action.

#### ![](https://www.researchgate.net/profile/Assad_Abbas/publication/272508863/figure/fig3/AS:294673521364994@1447267050155/A-Generic-Example-of-Content-Based-Filtering.png)

**2. Content Based Recommender:**
This option provided a lot of promise, but lacked a key feature that led us to our final decision. Content based recommenders are fantastic at finding similar content. However, in order to make a content-based recommender work, it needs a baseline article, movie, or variable to compare to other variables. This would not work if we wanted to follow our deliverable goals. When people come to our site, they do not have a specific article title in mind that the model can then classify and spit out similar articles.

<img src="flow_chart.png" >

**3. A Search Engine Based with Word2Vec Augmentation and a Content Based Recommender**  
In order to make up for the weaknesses of a content-based recommender the most logical conclusion is to create a search engine. The user needs to be able to search for not only the disaster but also the location. The search engine takes in a user's input, and using word vectors, the model creates a list of words similar to the user's input. Then the model compares the list of word2vec words to the keywords for each article. If the article meets a threshold for a certain number of keywords, then the search engine returns a list of those articles. We ended up choosing this one.

### Limitations:
- **The recommender system needs a baseline article to recommended similar articles**
    - The recommender system works by finding works with higher cosine scores. That does not work with a simple search term, but that was supplemented by the word2vec search engine.

- **Scraping**
    - This is probably our biggest limitation. Since pulling our articles from our initial webscrape, we did not scrape anymore articles. However, in the future we would want to find a way to connect the program to the internet.

- **Filters**
    - So far, we are only basing our model on keywords inputted from the user. Ideally, we would have drop down menus where the user could select type of information such as "damage assessment" or "evacuation routes"

- **Data Sources**
    - We scraped data from News API. It would be helpful to have a page for each disaster that would scrape the Twitter results for that search item as well as updates from a government agency all in one place. This leads to the user's situation awareness only developed from the news articles.



### Next Steps:

1. **Create a server and connect the data to the internet:**
    - If we could create a webscraping program that would scrape data for every search term, we could ensure we are getting the timeliest data for each disaster event.

2. **Scrape data from other mediums:**
    - Twitter and government agencies are a valuable resource for disaster specific information. Creating a webpage where a user's keywords would pull up the twitter data and latest updates from relevant government agencies would elevate the user's disaster awareness.

3. **Pair Traffic Data to find the best evacuation routes:**
    - During a major disaster, we want people to evacuate the area. This will create congestion on roads. In order to prevent panic, and to ensure everyone's safety, we want to create a map show the points of greatest congestion, and pair the map with another proven traffic app like Waze to get everyone out efficiently.

4. **Damage Assessment Page**
    - After a disaster strikes, first responders will have the Herculean task of finding and treating survivors as well as cleaning up hazardous materials. When people are using our program, we will create an input that will let us know if they have left their house. Comparing that with demographic and census data, first responders can then target their search efforts in high density population areas where the data shows residents did not evacuate. This will increase the likelihood of finding survivors and reduce loss of life.
    -Even more, we could create a map overlaid with the disasters path and points of greatest impact. For example, during a hurricane, the locations near the ocean are usually the hardest hit as the hurricane loses strength as it passes over land. Superimposing weather data over the map can show first responders the hardest hit areas.

5. **SummarizeBot API**
- While trying to choose what API to use. I came across this API that apparently sifts through fake news articles and conducts sentiment analysis on the articles. This would be interesting to explore, to sift through relevant articles and "fake news" articles.



### Conclusions:
With our combined effort, this is a good first step in creating a one-stop shop for disaster data. The word2vec search engine combined with a recommender system will pull up relevant data with similar efficiency to Google’s search engine. It allows the user to input keywords that correspond to keywords of relevant articles, which is an increased functional component not seen from past attempts. However, there is always room for improvement and there are many "Next Steps" that would increase the user's experience and site functionality.

### Word vectors
**To be able to use this codes, download:**
[Word Vectors](https://www.dropbox.com/s/kguufyc2xcdi8yk/lexvec.enwiki%2Bnewscrawl.300d.W.pos.vectors.gz?dl=1)

### Sources and References:

1. **Our Webscraper:**
 - [https://newsapi.org/](https://newsapi.org/)
2. **Inspiration for Our Search Engine:**
 - [https://towardsdatascience.com/lets-build-an-article-recommender-using-lda-f22d71b7143e](https://towardsdatascience.com/lets-build-an-article-recommender-using-lda-f22d71b7143e)
 - [https://towardsdatascience.com/how-we-built-a-content-based-filtering-recommender-system-for-music-with-python-c6c3b1020332](https://towardsdatascience.com/how-we-built-a-content-based-filtering-recommender-system-for-music-with-python-c6c3b1020332)
 -https://realpython.com/build-recommendation-engine-collaborative-filtering/
3. **Other Data Sources:**
 - [DSI-BOS 2019](https://github.com/mariellemarcus/New-Light-Technologies-Project)
 - [DSI-NY 2019](https://github.com/RMExe/disaster-web/)
 - [DSI-SF 2019](https://github.com/surajsakaram/NLT-Client-Project)
