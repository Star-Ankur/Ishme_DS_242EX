# Ishme_DS_242EX
## Instruction to running the code
Put the path locations in the code to the path location in which the data is stored
## Approach used
As the given data is time series it is shifted by p=1 and  used to calculate haversine distance using consecutive longitude and latitude.
Duration between this locations is calculated using timestamp.
This data is used to train Linear regressor and Random forest model.
