#!/usr/bin/python3
"""
Module for querying Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid
    """
    if not subreddit:
        return 0
    
    # Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # Make request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if response is successful (200 OK)
        if response.status_code != 200:
            return 0
        
        # Parse JSON response
        data = response.json()
        
        # Extract subscriber count
        subscribers = data.get("data", {}).get("subscribers", 0)
        
        return subscribers
    except (requests.RequestException, ValueError, KeyError):
        # Return 0 on any request or parsing errors
        return 0