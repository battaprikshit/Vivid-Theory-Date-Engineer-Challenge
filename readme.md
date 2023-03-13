Instructions to run the program:
1.From your console execute the following command: python datachallenge.py --filepath "location of csv file"

  for eg: python datachallenge.py --filepath "C:/Users/Prikshit Batta/Downloads/DataEngineer-Challenge.csv"


How to read the console output:

1. Rejected due to validation on input data:
	- Code will check that the vin is present and is string if its not it will show Rejected Vehicle failed for input data.
	- Code will check that the year is number if its not it will show Rejected Vehilcle failed for input data.
	- Code will check that the condition is "U" or "N"  or missing. If its not it will show Rejected Vehicle failed for input data.

2. Rejected due to validation on hey auto data:
	- Code will check that the data types of all the attributes and if it not according to the hey auto required data type then  it will show 	  	  	  Rejected Vehicle failed for hey auto input.
	- Code will check the validation as per the hey auto vaidation check.If it not according to the hey auto required validation then  it will show 	  	  Rejected Vehilcle failed for hey auto input.
	- Code will ensure that columns are only as per the data passed.

3. It will tell the Number of vehilces that failed the input data 

4. It will tell the Number of Vehicles that failed the hey auto data model

5. It will tell the vehicles that are accepeted by hey Auto data model.

