# 🎬 Movie Recommender System

यह एक Streamlit आधारित **Content-Based Movie Recommendation System** है जो चुनी गई फिल्म के आधार पर उससे मिलती-जुलती फिल्में सुझाता है। यह सिस्टम similarity matrix और movies dataset का उपयोग करता है।

---

## 📌 Features

* 🎯 Content-based movie recommendations
* 🔍 5000+ movies database सपोर्ट
* ⚡ Fast and lightweight Streamlit app
* 🎨 Clean UI with card-based output
* 📋 List view option for recommendations

---

## 🗂 Project Structure

```
project-folder/
│
├── app.py            # Main Streamlit application
├── movies.pkl        # Movie dataset (pickle file)
├── similarity.pkl    # Similarity matrix (pickle file)
├── README.md         # Project documentation
```

> नोट: आपकी स्क्रिप्ट में `similarity.pkl` Google Drive से लिंक के माध्यम से उपयोग हो रही है।

## 👨‍💻 Developer

**Ankit** [Instagram](https://www.instagram.com/__ankit._.op_/)

Python | Machine Learning | Streamlit

---

## ⚙️ Requirements

Python 3.8+ और निम्नलिखित लाइब्रेरी आवश्यक हैं:

```
streamlit
pandas
pickle
```

इंस्टॉल करने के लिए:

```bash
pip install streamlit pandas
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

एप चलने के बाद ब्राउज़र में मूवी सर्च करें और recommendations पाएं।

---

## 🔗 Google Drive Files

Similarity matrix Google Drive से लोड होती है:

```
File ID: 1xrydZhyakntow9_IZSmsx_bGEYQxVWCG
```

---

## 🧠 How It Works

1. User कोई movie select करता है।
2. सिस्टम उस मूवी का index खोजता है।
3. Similarity matrix से top 5 similar movies निकाले जाते हैं।
4. Streamlit UI में cards के रूप में results दिखते हैं।

---

## 🚀 Future Improvements

* Poster images add करना
* Genre based filtering
* User rating based recommendations
* Login system add करना

---

## 📜 License

यह प्रोजेक्ट educational purpose के लिए बनाया गया है। आप चाहें तो इसे MIT License के अंतर्गत release कर सकते हैं।

---


