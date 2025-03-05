from flask import Flask, render_template, request
from collections import Counter
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def extract_keywords(text, top_n=10):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    
    stop_words = set([
        "the", "is", "in", "and", "to", "a", "of", "for", "on", "with", "as", "by", "at", "it",
        "this", "that", "from", "was", "are", "but", "not", "be", "or", "an", "have", "has",
        "had", "can", "will", "would", "could", "should", "about", "which", "there", "so", "if"
    ])
    
    filtered_words = [word for word in words if word not in stop_words]
    keyword_counts = Counter(filtered_words)
    most_common_keywords = [word for word, _ in keyword_counts.most_common(top_n)]
    
    return most_common_keywords

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text() for p in paragraphs)
    except requests.exceptions.RequestException:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    keywords = None
    if request.method == "POST":
        text = request.form.get("text")
        file = request.files.get("file")
        url = request.form.get("url")

        if text:
            keywords = extract_keywords(text)
        elif file:
            file_content = file.read().decode("utf-8")
            keywords = extract_keywords(file_content)
        elif url:
            extracted_text = extract_text_from_url(url)
            if extracted_text:
                keywords = extract_keywords(extracted_text)
            else:
                keywords = ["Unable to extract text from URL."]

    return render_template("index.html", keywords=keywords)

if __name__ == "__main__":
    app.run(debug=True)
