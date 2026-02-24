#!/usr/bin/python3
"""
Module for querying Reddit API hot posts
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
    """
    if not subreddit:
        print("None")
        return
    
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Make request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if response is successful (200 OK)
        if response.status_code != 200:
            print("None")
            return
        
        # Parse JSON response
        data = response.json()
        
        # Extract the first 10 hot posts
        posts = data.get("data", {}).get("children", [])
        
        # Print the titles of the first 10 posts
        for i, post in enumerate(posts[:10]):
            title = post.get("data", {}).get("title", "")
            print(title)
    except (requests.RequestException, ValueError, KeyError):
        # Print None on any request or parsing errors
        print("None")