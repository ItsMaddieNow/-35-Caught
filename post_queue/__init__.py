from oauth2 import authorize

def Submit_Posts():

    oauth_key = authorize()
    parent_tumblelog_uuid = post["blog"]["uuid"]
    parent_post_id = post["id"]
    reblog_key = post["reblog_key"]
    reblog_url = "api.tumblr.com/v2/blog/{blog-identifier}/posts".format(Config.TUMBLR_BLOG_NAME)
    requests.post(reblog_url, params={"parent_tumblelog_uuid": parent_tumblelog_uuid, "parent_post_id": parent_post_id, "reblog_key": reblog_key}, headers={"Authorization": "Bearer {token}".format(token=self.tumblr_oauth_token)})
    