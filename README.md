
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
### Functions
1. Should only do one thing.
2. Must display an example output if applicable.
3. Must have docstrings, short explanation if needed, try-except statement, and logging outputs.
```
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
    if isinstance(number_1, bool) or isinstance(number_2, bool):
        raise ValueError
    result = float(float(number_1) + float(number_2))
    logging.info(f"Successfully added {number_1} and {number_2}. Result: {result}")
    return result
  except ValueError:
    if isinstance(number_1, str) or isinstance(number_1, bool):
      logging.warning(f" FIRST number not instance of int or float. Converting to zero.")
      number_1 = 0
    if isinstance(number_2, str) or isinstance(number_2, bool):
      logging.warning(f" SECOND number not instance of int or float. Converting to zero.")
      number_2 = 0
    return add(number_1, number_2)
  except Exception as e:
    logging.error(f" {e} caught in execution.")
```
## SQL Queries Standards
