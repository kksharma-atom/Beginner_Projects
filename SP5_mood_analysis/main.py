import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download("vader_lexicon")

# Iterate over the files in directory "diary"
# And store each file in dictionary
filepaths = sorted(glob.glob("diary/*.txt"))

files = {}
for filepath in filepaths:
    with open(filepath, "r") as file:
        files[Path(filepath).stem] = file.read()

# Create instance of SentimentIntensityAnalyzer class
analyzer = SentimentIntensityAnalyzer()

# Loop over each file in dictionary and assign positive 
# and negative score for each
positive_scores_list = []
negative_scores_list = []
for file in files:
    score = analyzer.polarity_scores(files[file])
    positive_scores_list.append(score["pos"])
    negative_scores_list.append(score["neg"])

date_list = sorted(files)

# Plot both the charts
st.title("Diary Tone")

st.subheader("Positivity")
figure_positive = px.line(x=date_list,
                 y=positive_scores_list, 
                 labels={"x": "Date", 
                         "y":"Positivity"} )
st.plotly_chart(figure_positive)

st.subheader("Negativity")
figure_negative = px.line(x=date_list,
                 y=negative_scores_list, 
                 labels={"x": "Date", 
                         "y":"Negativity"} )
st.plotly_chart(figure_negative)

