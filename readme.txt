How to Run

Navigate to the project folder:

cd sentiment_app


Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Enter text, click Analyze, and view sentiment, polarity, and subjectivity.


nstall Required Libraries
pip install flask textblob


If you haven't downloaded TextBlob corpora, run:

python -m textblob.download_corpora

2️⃣ Project Structure
sentiment_app/
│
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── requirements.txt