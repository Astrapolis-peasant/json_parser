# Json Parser

## Usage

make sure python is installed
```
git clone https://github.com/bonanyuan/json_parser 
cd parser
python parser_out.py
```
Then it will output all the results into different files in the same folder

## Intro
### 	stucture
The data stucture is basically an array of json objects. Therefore, we could read the file line by line streamingly.

### size of data
The size of the data is comparatively small. Any programing language should be able to easily parse it. I am using python here since it is my most familiar language.

### read and write the file streamingly
To minimize the memory usage, most rows are read and save line by line without saving into computer memory. 

## python package used
No third party packages have been used. Just three python native packages: `re`, `json`, `time`
### invalid rows
For the rows with invalid keys or info. I counted them and printed out them at the end

## Tasks

### Task 1
Created an empty dictionary to store all the keys as unique locality and values as the frequency of occurance.

###Task 2
Use regex to judge if the address starts with number. add it into `set()` if it is.

### Task 3
Use regex to judge if the address contains a number, write to file if it is not.

### Task 4
Simply judge if word 'museum' is in the categorical labels. `count+=1` if it is.

### Task 5
Created a new dictionary contain 4 keys, save to file

### Task 6
Use regex to find out the `"name":"xxxx"` and then change it to lower cases. We can not use `json.load` to get the string since dictionary is unordered, which will change the order of original json

### Task 7
Simply transfer the open time to `integer` and save the row if `open_time < 10`

## 	Conclusion
The entire task took around 0.06s in average to complete including create files, reading, parsing, saving and closing. It should be scalable with larger data sizes