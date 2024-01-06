import json
import tkinter as tk
import tkinter.ttk as ttk
from tkhtmlview import HTMLLabel
import config
import requests
import sqlite3
import post_reviewing.review_window as review_window


def review():

    app_config = config.Config()
    

    # SQLite3 database
    conn = sqlite3.connect("posts.db")
    c = conn.cursor()

    # Check if table exists if not create it
    c.execute("CREATE TABLE IF NOT EXISTS processed_posts(id INTEGER PRIMARY KEY)")
    c.execute("CREATE TABLE IF NOT EXISTS post_queue(post_id INTEGER PRIMARY KEY, parent_tumblelog_uuid TEXT, reblog_key TEXT, tags TEXT)")
    conn.commit()

    

    window = review_window.MyWindow("posts2.json", conn)
    window.mainloop()




if __name__ == "__main__":
    review()


    
    
            