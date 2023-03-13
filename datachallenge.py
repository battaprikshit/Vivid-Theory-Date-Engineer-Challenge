import argparse
import sys
import csv
from enum import Enum
from logging import getLogger
import logging
logging.basicConfig(level=logging.DEBUG)

class ConditionLevels(Enum):
      U = "Used"
      N = "New"

class InputVehicle: 
    def __init__(self,header,row):
        row_dict = dict(zip(header,row))       
        
        if self.validate_input(row_dict) :   
            self.__dict__ = dict(zip(header,row))      
    
    def validate_input(self,row_dict):
        if isinstance(row_dict["vin"], str) and len(row_dict["vin"]) >0 and isinstance(row_dict["make"], str) and isinstance(row_dict["model"], str) and (row_dict["year"].isdigit(), int) and isinstance(row_dict["trim"], str) and (row_dict["Condition"]  in [c.name for c in ConditionLevels] or len(row_dict["Condition"])==0) : 
            return True 
        else:      
            logging.warning(f"Rejected vehicle! Validation failed for input data: {row_dict}")    
            return False
               

class Vehicle: 
    def __init__(self,input_vehicle):
        vehicle = {}
        if self.validate_hey_auto(input_vehicle):
            vehicle["vin"]= input_vehicle.vin
            vehicle["make"]= input_vehicle.make
            vehicle["model"]= input_vehicle.model
            vehicle["year"]= int(input_vehicle.year)
            vehicle["trim"]= input_vehicle.trim
            vehicle["Condition"]= ConditionLevels[input_vehicle.Condition].value
            self.__dict__ = vehicle


     
    
    def validate_hey_auto(self,input_vehicle):
        if len(input_vehicle.vin) ==17 and len(input_vehicle.make) >0 and  len(input_vehicle.model)>0 and len(input_vehicle.year)>0 and (1990 <= int(input_vehicle.year) <=2024) and len(input_vehicle.Condition)>0:
            return True
        else:
            logging.warning(f"Rejected Vehicle! validation failed for hey Auto: {input_vehicle.__dict__}")    
            return False
               

def handler(argv):
    parser = argparse.ArgumentParser(description="ETL to ingest vehicle data to hey auto")
    parser.add_argument("--filepath",required=True,help="Location of the data file")
    args = parser.parse_args(argv)
    
    input_data = list(csv.reader(open(args.filepath)))
    header = input_data[0]    
    vehicle_data = []    
    for row in input_data[1:]:
        input_vehicle = InputVehicle(header,row)
        if input_vehicle.__dict__:         
            vehicle_data.append(input_vehicle)
            # print(input_vehicle.__dict__)
    logging.info ("Number of Input Vehicles which satisfy the input model: "+ str(len(vehicle_data)))
    
    hey_auto_vehicles=[]
    for input_vehicle in vehicle_data:
        vehicle = Vehicle(input_vehicle)  
        if vehicle.__dict__:         
            hey_auto_vehicles.append(vehicle)
            logging.info(f"Accepted vehicle! All Validation Passed: {vehicle.__dict__}")
    logging.info ("Number of Input Vehicles which satisfy the hey auto model: "+ str(len(hey_auto_vehicles)))


if __name__ == '__main__':
    handler(sys.argv[1:])
