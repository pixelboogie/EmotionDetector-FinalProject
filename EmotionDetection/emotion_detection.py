import requests 
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)         # Parsing the JSON response from the API

    if 'emotionPredictions' in formatted_response:
        # Extract the first item which contains the emotion predictions
        emotions_data = formatted_response['emotionPredictions'][0]
        emotions = emotions_data['emotion']
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Add dominant emotion to the dictionary
        emotions['dominant_emotion'] = dominant_emotion
        
        return emotions
    else:
        return None

'''
python3.11
import json
from emotion_detection import emotion_detector
emotion_detector("I am so happy I am doing this")
exit()

{"anger":0.0058758697,"disgust":0.0018923685,"dominant_emotion":"joy","fear":0.0048937234,"joy":0.9890151,"sadness":0.021380471}


'''
