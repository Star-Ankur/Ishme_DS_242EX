### Task
Create a model to estimate the travel time, in minutes, between source-destination pairs using the provided dataset.

### Background

-We have a dataset containing information about the buses travelling in Bengaluru obtained from Bengaluru Metropolitan Transport Corporation (BMTC).

-The data was collected from around two thousand buses for one day, between 7:00am to 7:00pm.

-The buses follow different routes within the city.

-Each bus is identified with a unique ID. A bus carries a device which records the data: latitude, longitude, speed, and timestamp.

### Dataset
We are given three files in the dataset (present in this repository in 'data' folder):

**BMTC.parquet.gzip**: It contains the GPS traces of around two thousand buses.

**Input.csv:** It contains geographical coordinates of various sources-destination pairs.

**GroundTruth.csv:** It contains the ground truth travel times between the source-destination pairs provided in Input.csv. 

### Instruction for running the code:

Download the files in the data folder from my repository. You need to make a small change in the Predict.ipynb script before running it.

```
df = pd.read_parquet('/content/drive/MyDrive/Data/BMTC.parquet.gzip', engine='pyarrow') 
dfInput = pd.read_csv('/content/drive/MyDrive/Data/Input.csv')
dfGroundTruth = pd.read_csv('/content/drive/MyDrive/Data/GroundTruth.csv')
```


In the above lines of code , you need to change the  path  to path where you have downloaded the the files of data folder.

###Data Insights

Every bus follows a specific route.Many buses have same route. Buses run through multiple times on their routes. 
                                                                     
### Approach used

As it was not possible to train the data on such large dataset .So we created a cluster of 105 buses that consisted of about 3,30,000 data points.The cluster was formed by grouping the data according to the bus ids and then The given data contained multiple rows when a bus was at halt.Only the first and last data of such rows were retained so that we can get information about halt time.
If the consecutive rows had same values of Latitude ,Longitude and speed we kept only the first and last rows.The given rows in the data set were just mere points we were not able to do anything with these. 
To associate a duration with the data points we created small segments combining consecutive rows.
Using this we created new attributes such as distance and duration in the dataframe.The distance attribute was computed by calculating **Haversine Distance** between coordinates of consecutive rows of dataframe and the duration to travel this distance was calculated using Timestamps.This way we divided the whole route into small segments so that we can analyse how much time is required to travel each small segment.This will also help to consider traffic conditions and other specific conditions that affect transit time in a particular locality.Then we used **linear regression and random forest** on this newly created dataset making duration as the target variable for training.*This model was used to make predictions on the Input csv and results were then compared with Ground truth csv.*

### References
https://www.researchgate.net/publication/334842116_Bus_travel_time_prediction_with_real-time_traffic_information
https://www.scitepress.org/Papers/2018/68163/68163.pdf
