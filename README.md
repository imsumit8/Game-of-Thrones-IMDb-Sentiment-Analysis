# Game-of-Thrones-IMDb-Sentiment-Analysis
This project involves conducting sentiment analysis on user-generated reviews of the renowned television series "Game of Thrones" sourced from IMDb. Leveraging the power of Natural Language Process. The data was meticulously collected through web scraping from a freely available source, Rapid API, ensuring a diverse and comprehensive dataset.
Certainly! Below is a format for a GitHub README file with two sections: "Importing the dataset using Webscraping from Rapid API" and "EDA and Sentiment Analysis." 

### Prerequisites
To obtain data from the IMDb database via RapidAPI, you'll need to start by registering for a free account on the RapidAPI portal. After registering, you can create a new application within your account, giving it a specific name and saving the details.

RapidAPI will then supply you with a unique API key, which is crucial for making requests to access the data. To use the IMDb API, navigate to the API hub and search for the desired API. Be sure to specify the application you created earlier and provide your API key for authentication.

Once you've subscribed to the API for testing purposes, you'll be ready to start requesting data from the IMDb database.


## Importing the dataset using Webscraping from Rapid API

```python
import requests
import csv

url = "https://imdb8.p.rapidapi.com/title/get-user-reviews"
querystring = {"tconst": "tt0944947"}
headers = {
    "X-RapidAPI-Key": "###########", #give your api key
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

# Create an empty list to store data
data_list = []

# Retrieve IMDb reviews data using a loop
for i in range(220):  # In each iteration, we get 25 reviews by hitting the API
    response = requests.get(url, headers=headers, params=querystring)
    API_Data = response.json()
    querystring["paginationKey"] = API_Data["paginationKey"]

    for review in API_Data["reviews"]:
        # Handle cases where certain fields may be missing
        authorRating = review.get('authorRating', None)
        helpfulnessScore = review.get('helpfulnessScore', None)

        data_list.append([
            review['id'],
            review['languageCode'],
            review['submissionDate'],
            review['reviewText'],
            authorRating,
            helpfulnessScore,
            review['spoiler']
        ])

# Save the collected data to a CSV file
with open('GOT_main.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_list)
```

## EDA and Sentiment Analysis
Data cleansing and preprocessing are essential initial steps in working with a dataset. Therefore, we conducted an Exploratory Data Analysis to obtain deeper insights into the dataset.
The project utilizes state-of-the-art NLP techniques, tokenizing and preprocessing the text data to enhance the quality of the sentiment analysis. Furthermore, the inclusion of stopwords removal ensures that common language artifacts do not influence the results.

By providing a nuanced understanding of the collective sentiment, the project opens the door to several insights. It can elucidate the aspects of the show that resonated most with viewers and shed light on any controversies or disappointments. These findings can be invaluable for content creators, media professionals, and even fans of the series.

### Exploratory Data Analysis (EDA)

In our Exploratory Data Analysis (EDA), we included descriptive statistics, handled null values, examined the distribution of numerical variables, presented a pie plot for categorical variables, assessed multicollinearity, and identified outliers.

### Sentiment Analysis
During our initial data preprocessing step, we began by converting all the text in the "reviewText" column to lowercase. Following this, we removed any special characters from the text. We then performed tokenization to break down the text into individual words and proceeded to eliminate common stop words from this list of words. Afterward, we isolated each word for emotion analysis. Utilizing the TextBlob library, we assessed the sentiment of each text in the column and calculated the polarity for the topics.

The **Polarity** is a floating-point value ranging between -1 and 1, where a **1** signifies a strongly positive sentiment, and a **-1** represents a significantly negative sentiment.

Therefore, they will play a significant role in assessing the online community's sentiment regarding the television series Game of Thrones.
++ FOR EDA AND SENTIMENT ANALYSIS ON DATASET RUN :
- [EDA+Sentiment Analysis on DATA](GOT-REVIEW-EDA+%20Sentiment_Analysis.ipynb)
  
### Year on Year Analysis



### Conclusion

The sentiment distribution analysis reveals intriguing insights about the reception of the TV series "Game of Thrones." Evidently, a substantial majority of reviews, approximately 78%, express a positive sentiment towards the show. This overwhelmingly favorable response reflects the widespread appeal and acclaim garnered by "Game of Thrones."

A noteworthy observation emerges when considering the ratings provided by reviewers. It becomes evident that a significant portion of the ratings falls within the range of 8 to 10. This concentration of high ratings reaffirms the series' popularity and the exceptional level of satisfaction it imparts to its viewers. The data implies that the show has effectively captured the hearts and minds of its audience, fostering a deeply positive sentiment among its viewers.

In summary, the sentiment analysis of "Game of Thrones" reviews underscores the remarkable extent of positive sentiment that surrounds the series. The preponderance of high ratings within the 8-10 range serves as a testament to its widespread popularity and success in eliciting enthusiasm and appreciation from its audience. This data attests to the enduring impact of the show and its ability to resonate with a broad and highly satisfied viewership.
## Contributions

Contributions are welcome to enhance the functionality and extend the use of this code for different analysis tasks. You can use this code for:

1. **Social Media Sentiment Analysis:** Extend this code to analyze sentiment on Twitter, Facebook, or other social media platforms by collecting and processing data from their APIs.

2. **Movie and TV Show Analysis:** Adapt the code to analyze sentiments, ratings, or reviews for other movies and TV shows from IMDb or other sources.

3. **Custom Analysis:** Use the code as a foundation for custom analysis tasks related to trending incidents, products, services, or any text data.

4. **Dependent Variable Definition:** Define suitable dependent variables for your analysis, such as user engagement, review ratings, or sentiment scores.

5. **Machine Learning Modeling:** Implement machine learning models on top of the sentiment analysis results to make predictions or gain deeper insights.

**Getting Started:**

- Fork this repository to your GitHub account.
- Clone the repository to your local environment.
- Customize the code to fit your specific analysis needs and data sources.
- Share your enhancements or analyses with the community by creating a pull request.

**Contributor Guidelines:**

- Follow open-source best practices and respect licenses and copyright.
- Ensure code quality and documentation in your contributions.
- Be respectful and collaborative in discussions and interactions.

By contributing to this project, you can help expand its utility for various analysis tasks and enable others to benefit from your expertise and insights.

## License

MIT License

Copyright (c) [2023] [Sumit Chowdhury]


## Acknowledgments

This project would not have been possible without the invaluable contributions of various open-source libraries and tools. We would like to express our gratitude to the following:

- [Matplotlib](https://matplotlib.org/) for creating data visualizations and plots.
- [NumPy](https://numpy.org/) for efficient numerical operations and array manipulation.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/) for natural language processing tasks.
- [Plotly](https://plotly.com/python/) for interactive and visually appealing data visualizations.
  
## Contact

For inquiries, feedback, or collaboration opportunities, feel free to contact me:

- Email: [imsumit8@gmail.com](mailto:imsumit8@gmail.com)

