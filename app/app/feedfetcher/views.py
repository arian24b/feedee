from django.shortcuts import render
from feedparser import parse


def parse_feed(url):
    # Parse the feed
    feed = parse(url)

    # Extract feed metadata
    feed_data = {
        'title': feed.feed.get('title', 'No title'),
        'link': feed.feed.get('link', 'No link'),
        'description': feed.feed.get('description', 'No description'),
        'entries': []
    }

    # Extract entries (individual feed items)
    for entry in feed.entries:
        feed_entry = {
            'title': entry.get('title', 'No title'),
            'link': entry.get('link', 'No link'),
            'published': entry.get('published', 'No publication date'),
            'summary': entry.get('summary', 'No summary')
        }
        feed_data['entries'].append(feed_entry)

    return feed_data


# Example usage:
url = 'https://example.com/feed'
feed_info = parse_feed(url)

# Print feed metadata
print(f"Feed Title: {feed_info['title']}")
print(f"Feed Link: {feed_info['link']}")
print(f"Feed Description: {feed_info['description']}")

# Print feed entries
for entry in feed_info['entries']:
    print("\nEntry Title:", entry['title'])
    print("Entry Link:", entry['link'])
    print("Published:", entry['published'])
    print("Summary:", entry['summary'])
