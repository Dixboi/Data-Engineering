
# Airways Data
## A data engineering project
### Background
Hello there! This is my data engineering project where I will apply specific concepts: making an ETL pipeline, data modeling, error handling, code standards, logging, and unit testing. This is where I will generally document my progress on learning and applying data engineering concepts.
### How can this repository help you
Possibly, you can see how I do or set the following:
- standardizing Python scripts and SQL queries
- data modeling
- create an ETL pipeline
- apply unit tests on a pipeline
### How can you help
- provide feedback on things that you think that needs improvement
## Table of Contents
- File Structure
- Data Model
- Data Pipeline
- Python Scripts Standards
- SQL Queries Standards
## File Structure
## Data Model
## Data Pipeline
## Python Scripts Standards
### Variable Names and Values
1. Boolean variable names should start with "is_" or "has_".
2. Boolean values should ONLY be "True" and "False" when stored in a database.
3. Date variable names should start with "date_".
4. Date values should be "YYYY-MM-DD"
### Functions
1. Should only do one thing.
2. Must display an example output if applicable.
3. Must have docstrings, short explanation if needed, try-except statement, and logging outputs.
```
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

def add(number_1, number_2):
  '''
  Add two numbers and return them as floats

  :param int/float: the first number
  :param int/float: the second number
  :return float: the sum of the first and second number in float type

  >>> add(4, 5)
  9.0
  '''
  try:
    result = float(number_1 + number_2)
  except Exception as e: # Catch all kind of errors
    logging.error(f" {e} caught in execution.")
  else:
    logging.info(f"Successfully added {number_1} and {number_2}. Result is {result}")
    return result
```
## SQL Queries Standards
