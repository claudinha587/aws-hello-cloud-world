import json
import os

def lambda_handler(event, context):
    
    
    weather_type = int(os.environ["WEATHER_TYPE"])
    
    
    if weather_type == 0:
        weather_type_str = "Cloudy"
    elif weather_type == 1:
        weather_type_str = "Snowy"
    elif weather_type == 2:
        weather_type_str = "Sunny"
    elif weather_type == 3:
        weather_type_str = "Windy"
    else:
        weather_type_str = "Unknown"
    
    body_mssg = "Hello "+ weather_type_str +" Cloud World from Lambda!"
    print (body_mssg)
    
    return {
        'statusCode': 200,
        'body': json.dumps(body_mssg)
    }
