from flask import Flask, render_template, request, flash
import pickle
import numpy as np
import logging
import gdown
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Google Drive file IDs
BOOKS_ID = "1OJBUiW0OEf7QFi4SlYFpJCDwydYc3W2S"
PT_ID = "1h6-MBfVXwJQom-bxFK_4dQ_qJXJtxdAx"
POPULAR_ID = "1ZoU1HT6KolNAXxUsU6NFHjNzv2GGPY19"
SIMILARITY_ID = "1v-D5QQwySQols9SIWPCkU_vr3FaGOhCL"

def download_if_not_exists(file_id, filename):
    """Download file from Google Drive if it doesn't exist locally"""
    if not os.path.exists(filename):
        logging.info(f"Downloading {filename}...")
        gdown.download(f"https://drive.google.com/uc?id={file_id}", filename, quiet=False)
    else:
        logging.info(f"{filename} already exists, skipping download")

# Download files from Google Drive
logging.info("Checking and downloading files from Google Drive...")
download_if_not_exists(BOOKS_ID, "books.pkl")
download_if_not_exists(PT_ID, "pt.pkl")
download_if_not_exists(POPULAR_ID, "popular.pkl")
download_if_not_exists(SIMILARITY_ID, "similarity_scores.pkl")

# Load data
logging.info("Loading data...")
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
logging.info("All data loaded successfully!")

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'ankit_super_secret_key_12345')

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           Votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           Votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values))

@app.route('/recommend_book', methods=['POST'])
def recommend_book():
    user_input = request.form.get('user_input')
    logging.info(f"User searched for: {user_input}")

    if user_input not in pt.index:
        flash("Book not found. Please try another title.", "warning")
        return render_template('recommend.html',
                               book_name=list(popular_df['Book-Title'].values),
                               author=list(popular_df['Book-Author'].values),
                               image=list(popular_df['Image-URL-M'].values),
                               Votes=list(popular_df['num_ratings'].values),
                               rating=list(popular_df['avg_ratings'].values))

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),
                           key=lambda x: x[1], reverse=True)[1:7]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    
    return render_template('recommend.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)