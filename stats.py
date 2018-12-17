import json_lines as jsonlines
import matplotlib.pyplot as plt
import seaborn as sns

hashtag_dict = {}
language_dict = {}
users = set()
text = set()
top_hashtags = set()
reduced = []

MAX=5000
simple_keys = ['created_at', 'full_text']

with jsonlines.open('brexit_tweets_all.jsonl') as reader:
    i = 0
    for tweet in reader:
        i += 1
        if tweet['lang']=='en':
            my_dict={}
            for key in simple_keys:
                my_dict[key]=tweet[key]
            my_dict['user_id'] = tweet['user']['id']
            my_dict['hashtags'] = tweet['entities']['hashtags']
            for hashtag in my_dict['hashtags']:
                hashtag['text'] = hashtag['text'].lower()
            my_dict['symbols'] = tweet['entities']['symbols']
            reduced.append(my_dict)
        if (i==MAX):
            break

for tweet in reduced:
    users.add(tweet['user_id'])
    text.add(tweet['full_text'])
    hashtags = tweet['hashtags']
    for hashtag in hashtags:
        hashtext = hashtag['text']
        try:
            hashtag_dict[hashtext] += 1
        except:
            hashtag_dict[hashtext] = 1
            
def dict_to_list(d, top = 50):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    return [x for _,x in sorted(zip(val,lbl), reverse = True)][:top]
            
print(dict_to_list(hashtag_dict))

tweets = []

for tweet in reduced:
    for h in tweet['hashtags']:
        if(h['text']=="voteleave"):
            print(tweet['full_text'])
            print("-")
            tweets.append(tweet['full_text'])

#for tweet in reduced:
#    v = 0
#    for h in tweet['hashtags']:
#        if(h['text']=="strongerin"):
#            v +=1
#        if(h['text']=="voteleave"):
#            v = -1
#    if(v==1):
#    print(tweet['full_text'])
#        print("-")
#        tweets.append(tweet['full_text'])

print(len(tweets))
            
def dict_to_hist(d):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    sns.set(style="darkgrid")
    ax = sns.barplot(x=lbl, y=val)
    fig = ax.get_figure()
    return fig

def dict_to_pie(d):
    lbl = []
    val = []
    for item in d.items():
        lbl.append(item[0])
        val.append(item[1])
    plt.pie(val, labels=lbl)


#fig = dict_to_hist(language_dict)
#fig.savefig('language_barplot.png')
#fig = dict_to_pie(hashtag_dict)
#fig.savefig('hashtag_barplot.png')

    
        
