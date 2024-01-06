import json
import requests
import time

import config

def pull():
    app_config = config.Config()

    tag = "dedf1sh"
    url = "https://api.tumblr.com/v2/tagged?tag={tag}"
    start = time.strptime("15 Sep 2023", "%d %b %Y")
    end = time.strptime("28 Feb 2023 1:00", "%d %b %Y %H:%M")
    start_timestamp = int(time.mktime(start))
    end_timestamp = int(time.mktime(end))



    start_time = time.time()
    posts = []
    end_reached = False
    while not end_reached:
        posts_request = requests.get(url.format(tag=tag), params={'before': start_timestamp, 'api_key': app_config.TUMBLR_CONSUMER_KEY})
        current_posts = json.loads(posts_request.text)['response']
        last_post_timestamp = int(current_posts[len(current_posts) - 1]['timestamp'])
        if last_post_timestamp < end_timestamp:
            end_reached = True
            for i in range(len(current_posts)-1,-1,-1):
                if int(current_posts[i]['timestamp']) >= end_timestamp:
                    for post in current_posts[0:i+1]:
                        posts.append(post)
                    break
        else:
            for post in current_posts:
                posts.append(post)
            start_timestamp = last_post_timestamp - 1
    print("--- Got {posts} posts in {time} seconds ---".format(posts=len(posts), time=(time.time() - start_time)))



    with open("posts.json", "w") as f:
        f.write(json.dumps({"posts": posts}, indent=4))
        f.close()



if __name__ == "__main__":
    pull()
