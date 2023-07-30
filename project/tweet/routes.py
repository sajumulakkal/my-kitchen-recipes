from . import tweet_blueprint
from flask import render_template, abort


tweet_post_titles = ['kitchenaid_mixer', 'measuring_cups', 'air_fryer']


@tweet_blueprint.route('/tweet/')
def tweet():
    return render_template('tweet/tweet.html')


@tweet_blueprint.route('/tweet/<tweet_title>/')
def tweet_posts(tweet_title):
    if tweet_title not in tweet_post_titles:
        abort(404)

    return render_template(f'tweet/{tweet_title}.html')


@tweet_blueprint.route('/about/')
def about():
    return render_template('tweet/about.html')
