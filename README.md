
# Data Engineering
## A repository to document my knowledge
### Background
Hello there! This is my data engineering project where I will apply all that I've learned from the [Data Engineering Carrer Track of DataCamp](https://app.datacamp.com/learn/career-tracks/data-engineer). The topics are making an ETL pipeline, data modeling, error handling, code standards, logging, and unit testing. Also, this is where I will generally document my progress on learning and applying data engineering concepts.
### How can this repository help you
Possibly, you can see how I do or set the following:
- standardizing Python scripts and SQL queries
- data modeling
- create an ETL pipeline
- apply unit tests on a pipeline
### How can you help
- provide feedback on things that you think that needs improvement
## Table of Contents
- General File Structure
- Python Scripts Standards
- SQL Queries Standards
## General File Structure
```
Project-
├── data/
|   ├── raw/
|   |   ├── extracted data one
|   |   L── extracted data two
|   |
|   ├── preprocessed/
|   |   ├── preprocessed data one
|   |   L── preprocessed data two
|   |
|   L── sample/
|       ├── sample data one
|       L── sample data two
|
├── documents/
|   ├── data model
|   ├── file structure
|   ├── pipeline
|   L── requirements
|
├── scripts/
|   ├── etl/
|   |   ├── extract
|   |   ├── transform
|   |   L── load
|   |
|   ├── qa/
|   |   ├── code profiling
|   |   ├── style checker
|   |   L── unit tests
|   |
|   L── main file
|
L── README.md
```
## Python Scripts Standards
### Variable Names and Values
1. Boolean variable names should start with "is_" or "has_".
2. Boolean values should ONLY be "True" and "False" when stored in a database.
3. Date variable names should start with "date_".
4. Date values should be "YYYY-MM-DD"
### Functions
1. Should only do one thing.
2. Must display an example output **if applicable**.
3. Must have docstrings, short explanation if needed, try-except statement, and logging outputs.
```
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def add(number_1, number_2):
    '''
    Add two numbers and return them as float

    Parameters
    number_1: int/float - the first number
    number_2: int/float - the second number

    Return
    result: float - the sum of the first and second number in float type

    Example
    >>> add(4, 5)
    9.0
    '''
    try:
        result = float(number_1 + number_2)
    except Exception as e:  # Catch all kind of errors
        logging.error(f"{e} caught in execution.")
    else:
        logging.info(f"Added {number_1} and {number_2} = {result}")
        return result

```
## SQL Queries Standards
- Should follow the [Modern SQL Style Guide](https://gist.github.com/mattmc3/38a85e6a4ca1093816c08d4815fbebfb)
```
select t1.name
     , t2.value
  from table_one as t1
  left join table_two as t2
    on t1.id = t2.id
 where t1.name like 'E%'
   and t2.value > 100
 order by t1.name
```
