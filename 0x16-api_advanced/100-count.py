#!/usr/bin/python3
"""Top ten"""
import requests

def count_words(subreddit, word_list):
    word_counts = {word: 0 for word in word_list}
    after = None

    while True:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'user-agent': 'MyAPI/0.0.1'}
        params = {'after': after, 'limit': 100}  # Increase 'limit' for more posts

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json().get('data')
            if not data:
                print("No data found. Check the subreddit name.")
                return

            after = data.get('after')
            children = data.get('children')

            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    word_counts[word] += title.split().count(word.lower())

            if after is None:
                break

        except requests.exceptions.RequestException as e:
            print("Request error:", e)
            return
        except ValueError:
            print("JSON parsing error")
            return

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_counts:
        if count:
            print(f"{word}: {count}")

# Example usage:
subreddit = "learnprogramming"
word_list = ["python", "programming"]
count_words(subreddit, word_list)

