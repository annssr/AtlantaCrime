# Atlanta Crime Mapping for CS7641 - Group 17
#### Abdurrahmane Rikli, Gabriel Leventhal-Douglas, Kevin Tynes, Aayush Dubey, and Sanjeev Prasada

![Atlanta Skyline](http://media.bizj.us/view/img/6139341/atlanta-skyline*750xx3684-2070-0-28.jpg)
# Introduction
## Motivation
In Atlanta, the overall crime rate is 108% higher than the national average. Crime is an ever-present concern. With almost 30 thousand crimes a year and a 61% crime rate per capita, Atlanta is one of the 3% most dangerous cities in the United States [1]. With such issues, the police force cannot deal with crime on a case-by-case basis. They need to be directed to crime-heavy areas preemptively.

#### What are you trying to do to tackle with your project motivation or problem?
Sufficient patrols in crime-heavy areas can be achieved using a prediction model to estimate the areas with the most severe crimes. More dangerous crimes can be preempted. With a real-time updating machine learning model, the police force can consistently catch up with crimes before they even occur day by day, and more often than not, their presence alone is enough to prevent crimes from occurring. Overall, as long as informative data is fed into the model, average crime rate is sure to consistently drop.

We reviewed literature of machine learning crime prediction methods using spatial [5, 3] and temporal [2] data in conjunction with crime-type. We will build upon this prior work by applying these methods to Atlanta crime data and improving predictive model efficiency.

#### What have people already done?
References are important. We may need to reference our proposal here and summarize our literature review. Will work on this tonight after dinner (post 9pm).
Crime statistics -likelihood for the most part- were pridected per 100k people in the state of Mississipi, irrespective of any features aside from the state's crime type statistics in their paper[2]. For the most part, time and space relevant features were examined only within the context of splitting areas into grids, and predicting intensity and displacement[3], although there were some attempts at clustering crime occurrences [5]. Closest to our approach was an attempt at predicting crime occurrences through similar features using KNN and Boosted Decision Tree, although the accuracy was 44% at its highest[4].

## Dataset (Needs description of features, accessability, etc.)
Our dataset comes from the Atlanta PD Crime Statistics dataset publicly available on [website](https://www.atlantapd.org/i-want-to/crime-data-downloads). This data is available as two separate datasets 'COBRA-2009-2018' and 'COBRA-2019'. After analyzing the Atlanta PD Crime dataset from 2009-2018, the most popular crimes in descending order are larceny from vehicle, larceny non vehicle, burglary at residence, and automobile theft. Our dataset is record-based; each row in the dataset represents one crime and the features of that crime (represented below in tables). We have a total of 20 features per record and a total of 317,905 records of crime within the Perimeter of Atlanta. There were a few columns we had to remove due a large number of null's and a few rows were removed based on inconsistency of data.


### Original Dataset

 Report Number | Occur Date | Occur Time | Neighborhood |   UCR Literal       | Latitude | Longitude 
 ------------- |:----------:|:----------:|:------------:|:-------------------:|:--------:|:---------:
 090010930     | 2009-01-01 |    1145    | Greenbriar   | LARCENY NON-VEHICLE | 33.69    | -84.49    
 090011083     | 2009-01-01 |    1330    | Downtown     | LARCENY NON-VEHICLE | 33.75    | -84.39    
 090011208     | 2009-01-01 |    1500    | Adamsville   | LARCENY NON-VEHICLE | 33.76    | -84.50    
 ...           |    ...     | ...        | ...          | ...                 | ...      | ...

### Unsupervised algorithms preprocessed dataset

Occur Date  | Neighborhood|   UCR Literal       | Latitude | Longitude  | Shift Occurrence 
 -----------|:-----------:|:-------------------:|:--------:|:----------:|:----------------:
 2009-01-01 | Greenbriar  | LARCENY NON-VEHICLE | 33.69    | -84.49     |  Day
 2009-01-01 | Downtown    | LARCENY NON-VEHICLE | 33.75    | -84.39     |  Day
 2009-01-01 | Adamsville  | LARCENY NON-VEHICLE | 33.76    | -84.50     |  Day
 ...        | ...         |    ...              | ...      | ...        |  ...  

### Supervised algorithms dataset

Year  | Month |  Day  | Day of Week  | Category 1 | Category 2 | Category 3 | Category 4 
 -----|:-----:|:-----:|:------------:|:----------:|:----------:|:----------:|:----------:
 2009 | 1     |   1   | 3            | 0          |  15        |    58      |  48
 2009 | 1     |   2   | 4            | 0          |  15        |    46      |  73
 2009 | 1     |   3   | 5            | 1          |  21        |    37      |  56
 ...  | ...   | ...   | ...          | ...        |  ...       |    ...     |  ...       

## Approach
It is important to cluster based on location and time, as they are relevant features of a crime’s occurrence and are useful for a police force’s patrol. Hence, the mean shift algorithm would be useful as one of the unsupervised learning methods to explore, in addition to k-means clustering. To finishAs for supervising learning techniques, decision trees have been used as a means of classification [2, 4]. Utilizing the severity of a crime served beneficial to the analysis. The decision tree works well, so naturally a random forest algorithm will supplement crime analysis further. Lastly, we can explore the accuracy given by a Naive Bayes Classifier. All algorithms need at least half of the available training data in order to build a successful set of clusters or prediction model to suffice for trends for crimes in future years, and to provide a police department with the necessary information on how they should run their patrol. Throughout our modeling and data pre-processing, we used primarily Python, along with a few Python packages: sci-kit learn, sci-py, pandas, and numpy.

#### Visualization of our crime-count original dataset. 

These visualizations of Atlanta are from the dataset 2009-2018 and are visualizing the counts of total crimes occuring.

![Atlanta all categories visualization](images/visualization/Crime_intensities.png?raw=true)

This is our visualization of our raw data. 

#### What is new in our approach?
We generated a crime score for each neighborhood for each day. This is our "secret sauce". We believe that in order to label locations as __hotspots__, we needed to aggregate a score including heavy weightage for the most severe crimes. We classified each crime that occured into one of these categories.

Here, we mention each category we created and what crimes fall into that category. Also, we are visualizing each category of crimes by itself in these plots.

+ Category 1: homicides, manslaughter     (1000x)

![Category 1](images/visualization/Crime_intensities_category_1.png?raw=true)

+ Category 2: aggravated assault, robbery  (100x)

![Category 2](images/visualization/Crime_intensities_category_2.png?raw=true)

+ Category 3: burgulary, auto-theft         (10x)

![Category 3](images/visualization/Crime_intensities_category_3.png?raw=true)

+ Category 4: larceny                        (1x)

![Category 4](images/visualization/Crime_intensities_category_4.png?raw=true)



## Visualization of Crime Scores
We would combine the weighted sum of crimes in a particular location and time to get the crime score of that area. For example, in 2019, the worst crime score was in 'Downtown' with a neighborhood score of 23254.

How we created the visualizations:
+ shapefile was imported in Python to read the shapefile data
+ pandas was to read the csv data
+ seaborn was used for coloring
+ matplotlib was to display the data (both pandas and shapefile)
+ need one paragraph explaining the legend and the conclusions we could make from the visualizations.

#### Actual 2019 visualization (Ground Truth)
![Crime Score 2019 Ground Truth](images/visualization/crime_scores_2019.png)
This first image is a visualization of our ground truth data from the 2019 dataset.

![Crime Score 2019 Prediction](images/visualization/crime_scores_2019prediction.png)
Here is our machine learning model's predicted 2019 data.

## Unsupervised Methods
Our tech stack for the unsupervised methods were sklearn in Python. First, we plotted the DBSCAN function and a corresponding elbow plot to __________ and optimize the ___________ and we conducted this method on k=3 to k=100. 
+ __Comment__ about what we learned through DBSCAN and drove the decision to also create __**DBSCAN Method 2** spatial representation__. 



+ __Comment__ about what DBSCAN reduced set told us about our data and what the reduced set aimed to do.

+ Mean shift is our next algorithm of choice. Mean shift results can vary as the bandwidth (radius) parameter is adjusted.

![Mean Shift](link)

We conducted PCA on the cobra-clean2009.csv and cobra-clean2019.csv dataset and received similar results. This shows that an almost identical amount of variance can be explained from the same components across different years. This shows the explained variance ratio is non-random and we have a justified reason to be using those Components.

![PCA explained ratio 2009](images/Unsupervised_Algs/PCA_cobra-clean2009.png)


![PCA explained ratio 2019](images/Unsupervised_Algs/PCA_cobra-clean2019.png)

## Supervised Methods
Our tech stack for the supervised methods were sklearn in Python. Some initial preprocessing is done with the data before the entered into the model. We utilize 10% of the data for testing, and 90% for training. This is the first time we use the Crime Score. We created this metric after obtaining domain knowledge of severity in crimes. Understanding the judicial system's consequences for certain crimes, we were able to manufacture a crime score for each neighborhood to took the severity of the crime into account. This is unique part of our project that aims to help map the toughest crime hotspots to police officers. 




#### Metrics & Results
1. Decision Tree
2. Random Forest
3. Naive-Bayes Classifier
4. Logistic Regression
5. Linear Regression

According to the location and time, specifically the neighorhood, day of the week, the month, and time in which the crime occurred, we are able to predict the most likely category of the crime and regress on the crime scores.

After our data was preprocessed, we built classification and regression methods using Decision Trees, Random Forest, Naive-Bayes, Linear Regression and Logistic Regression. We also performed Cross-Validation on all of the models and their respective time, accuracy/precision/recall metrics, and RMSE plots are displayed below. 

We attempted to do Support Vector Machine but it took way too long and had low performance. Because it led to unsatisfactory results, we removed it from our results section and chose to move forward.

When it comes to time, Naive-Bayes and Linear Regression are the two quickest algorithms that we ran, whereas Logistic Regression was the slowest. 

As for the accuracy metrics, Naive-Bayes Classifier and Logistic Regression were the only two methods that had a higher accuracy than the lower bound (0.55). The lower bound is calculated by classifying all data points as the most popular category, which was Category 4. However, logistic regression mostly classified every entry correctly as Category 4 (the recall is 0.999).

Lastly, the RMSE values showed that Random Forest had the lowest error, when regressing the crime scores. The highest RMSE value was from Logistic Regression. In conclusion, we prefer the Naive Bayes Classifier for determining the categories and Random Forest for calculating the crime scores.

![Metric 1](images/Supervised_Algs/apr_categories.png)

![Metric 2](images/Supervised_Algs/rmse.png)

![Metric 3](images/Supervised_Algs/times.png)

![Metric 4](images/Supervised_Algs/log_times.png)

## Discussion 
True crime prediction entails a complex set of variables that may not be publicly available for intrepid data scientists. Socioeconomic factors may be difficult to aggregate, while psychological motivators are highly abstract. Identification of crime hotspots allows law enforcement agencies to allocate police routes and other crime inhibiting factors, such as CCTV cameras, lights or neighborhood watches, more effectively [3]. Crime inciters, such as gang territories, bars, and construction sites can be monitored more frequently. 

We evaluated our approach using accuracy, precision, and recall for classification of categories. In regression of crime scores, our metric is RMSE.

## Conclusion

#### Major Achievement
Our major achievement was our supervised model using crime score. Naive Bayes Classifier was our metric of choice. NBC was the 2nd quickest to run, it was also the 2nd best accuracy as well. Logistic Regression classification gave us our best accuracy of 0.637. The predicted values would be 1, 2, 3, or 4 based on the day and neighborhood. Classification methods and metrics that are above the lower bound that we set for. 
#### Future work
Without question, our methodology could be improved. Given more time and resources, we would plan to merge our dataset with other datasets regarding Atlanta location specifics. Giving neighborhoods more features and more variability would only help our model learn and raise our accuracy. Another thing we would may be consider would be implementing similar prediction using deep learning neural networks.

Although we had access to 300,000+ rows of data, access to more data would make our model more robust.

## References 
[1] Schiller, Andrew. "Atlanta, GA Crime Rates & Statistics." NeighborhoodScout. NeighborhoodScout, 10 June 2019. Web. 30
Sept. 2019. </br>

[2] Mcclendon, Lawrence, and Natarajan Meghanathan. "Using Machine Learning Algorithms to Analyze Crime
Data." Machine Learning and Applications: An International Journal 2.1 (2015): 1-12. Print. </br>

[3] Lin, Ying-Lung, Meng-Feng Yen, and Liang-Chih Yu. "Grid-Based Crime Prediction Using Geographical Features."
ISPRS International Journal of Geo-Information 7.8 (2018): 298. Print. </br>

[4] Kim, Suhong, Param Joshi, Parminder Singh Kalsi, and Pooya Taheri. "Crime Analysis Through Machine Learning."
2018 IEEE 9th Annual Information Technology, Electronics and Mobile Communication Conference (IEMCON)
(2018): n. pag. Print. </br>

[5] Bappee, Fateha Khanam, Amílcar Soares Júnior, and Stan Matwin. "Predicting Crime Using Spatial Features."
Advances in Artificial Intelligence Lecture Notes in Computer Science (2018): 367-73. Print.




Contributions from each team member:
1. Gabriel Leventhal-Douglas: 100
2. Abdurrahmane Rikli: 100
3. Sanjeev Prasada: 100
4. Aayush Dubey: 100
5. Kevin Tynes: 100
