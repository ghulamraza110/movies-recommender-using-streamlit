# 🎬 Movie Recommender System (Streamlit App)

An interactive movie recommendation engine built with **Streamlit**, powered by content-based filtering using movie metadata. This app suggests similar movies based on plot, genre, cast, and keywords — and fetches posters via the TMDB API.

---

## 🚀 Live Demo

> https://movies-recommender-using-app.streamlit.app/

---

## 📦 Features

- 🔍 **Content-Based Recommendations** using cosine similarity
- 🧠 **Metadata Fusion**: overview, genres, keywords, cast, and director
- 🖼️ **Poster Fetching** via TMDB API
- 🎯 **Top 5 Similar Movies** displayed with titles and images
- ⚡ **Fast UI** built with Streamlit columns

---

## 🛠 Tech Stack

| Layer         | Tools Used |
|---------------|------------|
| **Frontend**  | Streamlit |
| **Backend**   | pandas, scikit-learn, nltk |
| **API**       | TMDB (The Movie Database) |
| **Storage**   | pickle (for precomputed data) |

---

## 📁 File Structure

```bash
├── app.py                 # Streamlit frontend
├── movie_dict.pkl         # Dictionary of movie metadata
├── similarity.pkl         # Cosine similarity matrix
├── movies.pkl             # Preprocessed movie DataFrame
├── tmdb_5000_movies.csv   # Raw movie metadata
├── tmdb_5000_credits.csv  # Raw cast and crew data
```

---

## 🧠 Recommendation Logic

```python
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    ...
```

---

## 🖼️ Poster Fetching

```python
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
```

> Replace `YOUR_API_KEY` with your TMDB API key.

---

## 📌 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/movie-recommender-streamlit
cd movie-recommender-streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 🔐 API Key Setup

- Sign up at [TMDB](https://www.themoviedb.org/)
- Get your API key
- Replace the placeholder in `fetch_poster()` with your key

---

## ✨ UI Preview

![App Screenshot](demo.png) <!-- Optional: Add a screenshot -->

---

## 📚 Credits

- TMDB dataset via Kaggle
- TMDB API for poster fetching
- Streamlit for rapid UI development

---
