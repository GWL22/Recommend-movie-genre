Recommend-movie-genre
- This project is movie genre recommend system using text analysis.
- I. data
 - The data crawled from [NaverMovie](http://movie.naver.com/) is saved on DB(in my case, MYSQL)
 - After reading some comments, assumed that the data over 7 points generally had enough expression to analyze easily
 - Because above the reason, Comments gave over 7 points in the data are used to analyze
- II. Preprocess
 - I) Tokenize
   - To do text analysis about sentence, the sentence should be decomposed
   - By doing that, it can be possible to distinguish between homonym
   - In my case, Twitter in Konlpy is applied
     - this is because comment has some similarity with twit
 - II) Doc2Vec
  - Doc2Vec makes documnet vector to be learned as word
 - III) Vectorize
  - CountVectorize: Count words 
  - TfidfVectorize: Count words + set weight
- III. Modeling
 - Used **2 types of preprocessed data: Vectorize, Doc2Vec**
 - For the first type, LogisticRegression and SVC is used
 - For the second type, DecisionTree, LogisticRegression, SVC, MultinomialNB
- IV. Conclusion
 - average score of Count+LogisticRegression is higher than Tfidf+kernel SVC
 - In the classification report, Tfidf+kernel SVC got better score
 - The best score was not over 80%.
 - It means that it is difficult to recommend genre by analyzing comments
- V. Limitation
 - There are about 300,000 data in train_jup.csv
 - For the memory problem, Only 20,000 data is used to analyze.
 - If whole data used, result could be changed

# Enviornment
- Python 2.7.12
- Package : Konlpy, NLTK

# Reference
https://www.lucypark.kr/slides/2015-pyconkr/#39
