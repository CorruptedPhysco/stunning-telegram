from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_target_link():
    # Target URL to scrape
    url = "https://bingotingo.com/best-social-media-platforms/"
    
    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"Failed to fetch the page. Status code: {response.status_code}"

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <a> tag with id="tool"
    link_element = soup.find("a", id="tool")
    if link_element:
        return link_element.get("href"), None
    else:
        return None, "Target link not found"

@app.route('/scrape', methods=['GET'])
def scrape():
    link, error = scrape_target_link()
    if link:
        return jsonify({"status": "success", "link": link})
    else:
        return jsonify({"status": "error", "message": error})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
