import json
import re
import time

def parser(json_file,outputfile):    
    #initalization variables
    dic_locality = {} #task1
    dic_locality_invalid = 0 

    addresses_start_number = set([]) #task2
    addresses_invalid = 0

    number_museums = 0 #task4
    category_labels_invalid = 0
 
    rows_with4_invalid =0 #task5

    hours_invalid = 0 #task7


    with open(json_file) as data: #read data
        for row in data: 
            st = json.loads(row) #parse the data by record into json

            try: #task1
            # get occurance of each city
                city = st['payload']['locality']
                dic_locality[city] = dic_locality.get(city,0)+1
            except KeyError:
                dic_locality_invalid+=1 #count records with invalid 'locality'

            try: #task2
                address = st['payload']['address']
                if re.search('^\s*\d',address): # get all addresses starts with number using regex
                    addresses_start_number.add(address)
                #task3
                if not re.search(r'\d',address): # get all addresses without number using regex
                    outputfile['task3'].write(row) 
            except KeyError:
                addresses_invalid+=1 #count records with invalid 'address'

            try: #task4
                if 'Museums' in st['payload']['category_labels'][0]: #check  if museum in labels
                    number_museums+=1 #count
            except KeyError:
                category_labels_invalid+=1 #count rows with invalid category labels

            try: #task5
                new_obj={'uuid':st['uuid'],'name':st['payload']['name'],\
                  'website':st['payload']['website'], 'email':st['payload']['email']} #create new dic for new object
                outputfile['task5'].write(json.dumps(new_obj)+'\n') # write to file
            except KeyError:
                rows_with4_invalid+=1 #count rows with incomplete 4 keys

            try : #task6
                new_row = re.sub('"name":"(.*?)"', lambda m: m.group().lower(),row) #change to lowercase if existed
                outputfile['task6'].write(new_row) #save to file
            except:
                output_file['task6'].write(row) #write the original row if not existed

            try: #task7
                if int(json.loads(st['payload']['hours'])['sunday'][0][0].split(':')[0])<10: #check if the start_hour<10
                    outputfile['task7'].write(row) #write to file
            except KeyError:
                hours_invalid+=1

        outputfile['task1'].write(json.dumps(dic_locality))
        outputfile['task2'].write(json.dumps(list(addresses_start_number)))
        outputfile['task4'].write(json.dumps(number_museums))

        # print out the number of missing values
        print 'number of rows with invalid locality: {}'.format(dic_locality_invalid)
        print 'number of rows with invalid address: {}'.format(addresses_invalid)
        print 'number of rows with invalid category_labels: {}'.format(category_labels_invalid)
        print 'number of rows with incomplete 4 keys: {}'.format(rows_with4_invalid)
        print 'number of rows with invalid hours on sunday: {} '.format(hours_invalid)

if __name__ == "__main__":
    start_time = time.time()
    output_file = {}
    for task in range(7): # open files to store the results
        output_file['task{}'.format(task+1)] = open('output_task{}'.format(task+1),'w') #store the openfile objects into dic
    
    parser('data.json',output_file) # run the function to write to files

    for task,out_file in output_file.iteritems():
        out_file.close()  #close all the opened files
    
    print 'parse complete! Time cousumed: {}'.format(time.time()-start_time) # count the time
