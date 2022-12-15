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
[Click to view the approach we used in detail.](https://docs.google.com/document/d/1yuy11cfP6FC4a8llFTEoOpWIL79jCH24e_oZ80vzVcU/edit?usp=sharing)
