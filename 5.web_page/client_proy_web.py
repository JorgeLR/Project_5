from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from rake_nltk import Rake
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity, linear_kernel
import gensim
app = Flask(__name__)

# Preparing CSV for HTML code
def get_url(url):
    return "/".join(str(url).split("/",3)[:3])

home_fire = pd.read_csv("../4.search_home/fire_home.csv")
home_fire["url_main"] = home_fire["url"].map(get_url)
home_fire = home_fire.to_dict('records')

home_torn = pd.read_csv("../4.search_home/torn_home.csv")
home_torn["url_main"] = home_torn["url"].map(get_url)
home_torn = home_torn.to_dict('records')

home_flood = pd.read_csv("../4.search_home/flood_home.csv")
home_flood["url_main"] = home_flood["url"].map(get_url)
home_flood = home_flood.to_dict('records')

home_earth = pd.read_csv("../4.search_home/earth_home.csv")
home_earth["url_main"] = home_earth["url"].map(get_url)
home_earth = home_earth.to_dict('records')

home_hurr = pd.read_csv("../4.search_home/hurr_home.csv")
home_hurr["url_main"] = home_hurr["url"].map(get_url)
home_hurr = home_hurr.to_dict('records')

news_fire = pd.read_csv("../3.final_data/fire_comb.csv")
news_fire["url_main"] = news_fire["url"].map(get_url)
news_fire = news_fire.to_dict('records')

news_torn = pd.read_csv("../3.final_data/tornado_comb.csv")
news_torn["url_main"] = news_torn["url"].map(get_url)
news_torn = news_torn.to_dict('records')

news_flood = pd.read_csv("../3.final_data/flood_comb.csv")
news_flood["url_main"] = news_flood["url"].map(get_url)
news_flood = news_flood.to_dict('records')

news_earth = pd.read_csv("../3.final_data/earthquake_comb.csv")
news_earth["url_main"] = news_earth["url"].map(get_url)
news_earth = news_earth.to_dict('records')

news_blizz = pd.read_csv("../3.final_data/blizzard_comb.csv")
news_blizz["url_main"] = news_blizz["url"].map(get_url)
news_blizz = news_blizz.to_dict('records')

news_hurr = pd.read_csv("../3.final_data/hurricane_comb.csv")
news_hurr["url_main"] = news_hurr["url"].map(get_url)
news_hurr = news_hurr.to_dict('records')

model = gensim.models.KeyedVectors.load_word2vec_format('../lexvec.enwiki+newscrawl.300d.W.pos.vectors')

def art_test(df, vars):
    search = vars
    stripped = [x.strip() for x in search.split(' ')]
    result = [x.lower() for x in stripped]
    print(result)
    word2vec_list = []
    for x in model.most_similar(result):
        term,sim = x
        word2vec_list.append(term)
    word2vec_list.extend(result)
    print(word2vec_list)
    article_list = []
    threshold = 7
    print(threshold)
    while len(article_list) < 5 and threshold > 3:
        for article in df.loc[df['keywords'].map(lambda x: sum(1 for w in word2vec_list if w in x)) == threshold, 'title']:
            article_list.append(article)
        threshold -= 1
    return article_list if len(article_list) > 0 else print('No Results!')


@app.route('/')
def home():
    return render_template('home.html', home_fire=home_fire, home_torn=home_torn, home_flood=home_flood, home_earth=home_earth, home_hurr=home_hurr)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/wildfire')
def wildfire():
    return render_template('wildfire.html', title='Wildfire', news_fire=news_fire)

@app.route('/tornado')
def tornado():
    return render_template('tornado.html', title='Tornado', news_torn=news_torn)

@app.route('/flood')
def flood():
    return render_template('flood.html', title='Flood', news_flood=news_flood)

@app.route('/earthquake')
def earthquake():
    return render_template('earthquake.html', title='Earthquake', news_earth=news_earth)

@app.route('/blizzard')
def blizzard():
    return render_template('blizzard.html', title='Blizzard', news_blizz=news_blizz)

@app.route('/hurricane')
def hurricane():
    return render_template('hurricane.html', title='Hurricane', news_hurr=news_hurr)

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    search_df = pd.read_csv('../3.final_data/mega_data.csv')
    search_list = art_test(search_df, variable)
    search_df["final_list"] = search_df["title"].map(lambda x: 1 if x in search_list else 0)
    search_df = search_df.loc[search_df["final_list"] == 1]
    search_df.to_csv("../4.search_home/search.csv", index= False)
    # Finish search CSV creation
    news_search = pd.read_csv("../4.search_home/search.csv")
    def get_url(url):
        return "/".join(str(url).split("/",3)[:3])
    news_search["url_main"] = news_search["url"].map(get_url)
    news_search = news_search.to_dict('records')
    # return variable
    return render_template('search.html', title='Search', news_search=news_search)

if __name__ == "__main__":
    app.run(debug=True)
