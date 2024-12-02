from flask import Flask, jsonify
from main import scrape_target_link

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    try:
        link = scrape_specific_link()
        return jsonify({"status": "success", "link": link})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
