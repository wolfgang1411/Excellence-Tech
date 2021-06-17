import requests
import json

posts = requests.get("https://my-json-server.typicode.com/typicode/demo/posts").json()
comments = requests.get("https://my-json-server.typicode.com/typicode/demo/comments").json()

for post in posts:
  for comment in comments:
      if post.get("id") == comment.get("postId"):
          if "comments" not in post:
            post.update({"comments":[]})
          comments = post.get("comments")
          comments.insert(1,{"body":comment.get("body"),"id":comment.get("id")})

for post in posts:
    print(post)