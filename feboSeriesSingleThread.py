import json

def lambda_handler(event, context):
    # TODO implement
    a = 1
    b = 1
    c = 0
    for i in range(3,10000) :
        c = a + b
        a = b
        b = c
    a = 1
    b = 1
    c = 0
    for i in range(3,20000) :
        c = a + b
        a = b
        b = c
    a = 1
    b = 1
    c = 0
    for i in range(3,30000) :
        c = a + b
        a = b
        b = c
    
    a = 1
    b = 1
    c = 0
    for i in range(3,40000) :
        c = a + b
        a = b
        b = c
    
    a = 1
    b = 1
    c = 0
    for i in range(3,50000) :
        c = a + b
        a = b
        b = c
    
    a = 1
    b = 1
    c = 0
    for i in range(3,60000) :
        c = a + b
        a = b
        b = c
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

