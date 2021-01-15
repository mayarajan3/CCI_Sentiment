# SLSProject

## Getting Sentiment Scores
Run the `get_scores.py` file to calculate sentiment scores using the NLP model found here: https://github.com/xiaohan2012/twitter-sent-dnn.

The script will require [Selenium](https://selenium-python.readthedocs.io/) and a copy of the [chrome webdriver](https://chromedriver.chromium.org/downloads) within the working directory to run.

An average sentiment is then calculated for each neighborhood, and `all_scores.json` as well as `average_scores.json` will be exported into the working directory. 

## Visualizing Sentiments
After running `visualize.py`, a list of statistics will be printed to the console. Additionally, the results/graphs/ folder will be populated with a graph for each NPU visualizing the average sentiment of each neighborhood.
