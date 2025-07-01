#!/usr/bin/env python3
import sys
import requests


def check_url_availability(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Resource {url} is network reachable, status code: {response.status_code}")
        sys.exit(0)
    except requests.exceptions.RequestException as e:
        print(f"Network error accessing {url}: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_availability.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    check_url_availability(url)