#*End to End Machine Learning Project - MovieOrbit* , 
A personalized movie recommendation system built using tmdb dataset.


##Features: 
```1.Content Based Filtering using movie metadata like genres,keywords,cast,crew and overviews.
2.Used Stemming and Text Normalization to uinfy similar words (like "love","loved" into "love")
3.Created combined "tags" column for each movie,aggregating all cleaned textual features.
4.Vectorized this corpus using "CountVectorizer" with a custom max feature size.
5.Finally , used Cosine Similarity to compute similar movies based on the cosine distance in high dimensional space.
```


##Stack and Tools:
-Python(pandas,numpy,sklearn,nltk)
-Streamlit for UI
-TMDB API for fetching movie posters
