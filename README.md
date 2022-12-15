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

### Instruction to running the code
Put the path locations in the code to the path location in which the data is stored
### Approach used
As the given data is time series it is shifted by p=1 and  used to calculate haversine distance using consecutive longitude and latitude.
Duration between this locations is calculated using timestamp.
This data is used to train Linear regressor and Random forest model.
