# vaxxAId

A machine project by Team BIRD in fulfillment of the requirements in CS 180 (Artificial Intelligence).

1. Aquitania, Rene Lee
2. Diokno, Alyssa Beatrice
3. Martirez, Derryn Joi
4. Yao, Marie Isabel

**DATASETS**
2021VAERSDATA.csv
2021VAERSVAX.csv
2022VAERSDATA.csv
2022VAERSVAX.csv

Note: The VAERSDATA files contain information on the patients such as sex, age group, state of residence, allergies, description of adverse effect, etc.The VAERSVAX files contain information about the vaccine administered on the patient, such as vaccine manufacturer, anatomic site where vaccine was administered, etc.

**DATA SOURCES**
Vaccine Adverse Effect Reporting System (VAERS) VAERS - Data Sets (hhs.gov)


**Outline**

**PART 1: Data Processing**

1.1 Importing the Libraries
1.2 Data Cleaning
1.3 Data Transformation
    mapping of nominal features into numerical labels

**PART 2: Exploratory Data Analaysis**

2.1 Univariate Analysis
    explores each variable in a data set and contains charts to visualize the collected data

**PART 3: Model Implementation**

3.1 Optimization of Number of Clusters
3.2 K-modes Clustering Model
    To perform K-modes clustering, the kmodes library from PyPI was used. The model uses the dissimilarities between the data points to identify the clusters. 
