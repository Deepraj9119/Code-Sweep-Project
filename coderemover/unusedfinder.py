import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """Checks if the given URL is a valid HTTP or HTTPS URL."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and parsed.scheme in ("http", "https")

def get_unused_resources(url):
    """Identifies unused resources on a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = urljoin(url, '/')
        resources = set()

        # Extract all resources
        for tag, attr in [('a', 'href'), ('img', 'src'), ('script', 'src'), ('link', 'href'), ('source', 'src'), ('iframe', 'src'), ('audio', 'src'), ('video', 'src')]:
            for element in soup.find_all(tag, **{attr: True}):
                absolute_url = urljoin(base_url, element[attr])
                if is_valid(absolute_url):
                    resources.add(absolute_url)

        # Check if resources are used in the HTML
        unused_resources = []
        html_content = response.text
        for resource in resources:
            if resource not in html_content:
                unused_resources.append(resource)

        print(f"Unused resources on {url}:")
        return unused_resources
            # return unused

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     target_url = 'https://thestudyvarta.blogspot.com/'
#     get_unused_resources(target_url)