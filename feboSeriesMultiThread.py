import json
import boto3
import threading

def calculate_feb(num):
    a = 1
    b = 1
    c = 0
    for i in range(3,num) :
        c = a + b
        a = b
        b = c
    
def lambda_handler(event, context):
    # TODO implement
    n = 6
    a = 1
    b = 1
    c = 0
   # json_requestBody = json.dumps(event)
    #print ("Request body:\n" + json_requestBody)
    t1 = threading.Thread(target=calculate_feb, args=(10000,))
    t2 = threading.Thread(target=calculate_feb, args=(20000,))
    t3 = threading.Thread(target=calculate_feb, args=(30000,))
    t11 = threading.Thread(target=calculate_feb, args=(40000,))
    t22 = threading.Thread(target=calculate_feb, args=(50000,))
    t33 = threading.Thread(target=calculate_feb, args=(60000,))
    
    t1.start() 
    t2.start() 
    t3.start() 
    t11.start() 
    t22.start() 
    t33.start() 
    
    t1.join() 
    t2.join() 
    t3.join() 
    t11.join() 
    t22.join() 
    t33.join() 
    
    
    #json.dumps('Hello from Lambda!')
    return {
        'statusCode': 200,
        'body': c
    }

