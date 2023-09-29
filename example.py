import cachetools
import mongomock
import requests
import requests_mock


if __name__ == "__main__":
    for module in cachetools, mongomock, requests, requests_mock:
        print(f"{module.__name__}: {module.__file__}")

