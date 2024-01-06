
import csv
import json


def convert():
    with open("posts.json", "r") as posts_json:
        posts = json.loads(posts_json.read())['posts']
        posts_json.close() 
        
        with open("posts.csv", "w") as posts_csv:
            field_names = ["blog", "post_url", "tags", "date", "timestamp"]
            writer = csv.DictWriter(posts_csv, fieldnames= field_names)
            writer.writeheader()

            for post in posts:
                writer.writerow({"blog": post["blog_name"], "post_url": post["short_url"], "tags": ",".join(post["tags"]), "date": post["date"], "timestamp": post["timestamp"]})
            posts_csv.close()


if __name__ == "__main__":
    convert()