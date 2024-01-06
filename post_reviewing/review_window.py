import json
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
import requests
from tkhtmlview import HTMLLabel
#from config import Config


class MyWindow(tk.Tk):
    def __init__(self, posts_path="posts2.json", tumblr_oauth_token="", conn=None):
        super().__init__()
        self.posts_path = posts_path
        with open(posts_path, "r") as f:
            self.posts = json.load(f)['posts']
            f.close
        if conn is None:
            conn = sqlite3.connect("posts.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS processed_posts(id INTEGER PRIMARY KEY)")
            c.execute("CREATE TABLE IF NOT EXISTS post_queue(post_id INTEGER PRIMARY KEY, parent_tumblelog_uuid TEXT, reblog_key TEXT, tags TEXT)")
            conn.commit()
        self.conn = conn
        self.tumblr_oauth_token = tumblr_oauth_token

        self.title("Review Posts")
        tags_frame = ttk.Frame(self)
        self.tags_label = ttk.Label(tags_frame, text="Tags", justify=tk.LEFT                                                                                                                                                                                                         )
        self.tags_entry = tk.Text(tags_frame, wrap=tk.WORD, width=30)
        
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_post)
        self.next_button = ttk.Button(self, text="Next Post", command=self.next_post)
        self.save_button = ttk.Button(self, text="Save Posts", command=self.save_posts)
        self.post_view = HTMLLabel(self, html="<p><figure class=\"tmblr-full\"><img src=\"https://64.media.tumblr.com/b93094987c6e6896046d8dd845140458/8241c3dc01266747-e1/s640x960/2820b9fdd95c28bd79dbb8fb07dd793d5472a469.jpg\" alt=\"image\" class=\"\"/></figure><figure class=\"tmblr-full\"><img src=\"https://64.media.tumblr.com/d58d2b610cc8fb930d6248009dd4dec4/8241c3dc01266747-14/s640x960/953a4c3249390dbdcd97dc6ddcc8dcd7319cfcfe.jpg\" alt=\"image\" class=\"\"/></figure><p>GOT MY CHARM FROM <a href=\"https://tmblr.co/MPMx9j6a5XgAd2FcRhmG-HA\">@shinesurge</a> it&rsquo;s so pretty!! Thank you so much again!!</p></p>")

        tags_frame.grid(row=0, column=0, sticky=tk.NSEW, columnspan=3, padx=2, pady=2)
        self.tags_label.pack(side=tk.LEFT)
        self.tags_entry.pack(side=tk.RIGHT)
        self.submit_button.grid(row=1, column=0, pady=2, padx=2)
        self.next_button.grid(row=1, column=1, pady=2, padx=2)
        self.save_button.grid(row=1, column=2, pady=2, padx=2)
        self.post_view.grid(row=0, column=3, sticky=tk.NSEW, rowspan=2, pady=2, padx=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        while True:
            if self.post_exists(self.posts[0]["id"]):
                self.posts.pop(0)
            else:
                break
        self.load_post(self.posts[0])
    
    def save_posts(self):
        with open(self.posts_path, "w") as f:
            f.write(json.dumps({"posts": self.posts}))
            f.close()
    
    def post_exists(self, post_id):
        c = self.conn.cursor()
        c.execute("SELECT id FROM processed_posts WHERE id=?", (post_id,))
        return c.fetchone() is not None

    def next_post(self):
        self.conn.cursor().execute("INSERT INTO processed_posts VALUES (?)", (self.posts[0]["id"],))
        self.conn.commit()
        self.posts.pop(0)

        while True:
            if self.post_exists(self.posts[0]["id"]):
                self.posts.pop(0)
            else:
                break
        
        self.load_post(self.posts[0])

    
    def load_post(self, post):
        self.tags_entry.delete("1.0", tk.END)
        self.tags_entry.insert("1.0", "{poster},dedf1sh,35 caught".format(poster=post["blog_name"]))
        self.post_view.set_html(post["body"])

    def submit_post(self):
        post = self.posts[0]
        self.conn.cursor().execute("INSERT INTO post_queue VALUES (?, ?, ?, ?)", (post["id"], post["blog"]["uuid"], post["reblog_key"], self.tags_entry.get("1.0", tk.END)))
        self.conn.commit()
        self.next_post()
    





if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()
