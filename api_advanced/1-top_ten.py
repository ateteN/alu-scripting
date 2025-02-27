import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json"
    HEADERS = {"User-Agent": "my_reddit_bot/1.0"}
    PARAMS = {"limit": 10}  # Get only the first 10 posts

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS, allow_redirects=False)
        
        # Check if the request was successful
        if RESPONSE.status_code == 200:
            posts = RESPONSE.json().get("data", {}).get("children", [])
            if posts:
                for post in posts:
                    print(post["data"]["title"])
            else:
                print(None)  # No posts found
        else:
            print(None)  # Invalid subreddit or error

    except requests.RequestException:
        print(None)  # Network or request error


