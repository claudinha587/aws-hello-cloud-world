import json
import os

def lambda_handler(event, context):
    
    
    world_type = os.environ["WORLD_TYPE"] 
    
    if world_type == 0:
        world_type_str = 'Cloudy'
    elif world_type == 1:
        world_type_str = 'Snowy'
    elif world_type == 2:
        world_type_str = 'Sunny'
    else:
        world_type_str = 'Windy'
    
    body_mssg = 'Hello '+ world_type_str +' Cloud World from Lambda!'
    print (body_mssg)
    
    return {
        'statusCode': 200,
        'body': json.dumps(body_mssg)
    }
