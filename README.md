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
                                                                     
### Approach used

In the **preprocessing** step if the consecutive rows had same values of Latitude ,Longitude and speed we kept only the first and last rows.Then with new dataframe first we created a lag of p=1 and appended the lagged dataframe with the preprocessed input dataframe.This gave us the consecutive coordinates of Longitude and Latitude in a single row.Using this we created new attributes such as distance and duration in the dataframe.The distance attribute was computed by calculating **Haversine Distance** between coordinates of consecutive rows of dataframe and the duration to travel this distance was calculated using Timestamps.This way we divided the whole route into small segments so that we can analyse how much time is required to travel each small segment.This will also help to consider traffic conditions and other specific conditions that affect transit time in a particular locality.Then we build **linear regression and random forest model** on this newly created dataset making duration as the target variable for training.*This model was used to make predictions on the Input csv and results were then compared with Ground truth csv.*

### References
https://www.researchgate.net/publication/334842116_Bus_travel_time_prediction_with_real-time_traffic_information
https://www.scitepress.org/Papers/2018/68163/68163.pdf
