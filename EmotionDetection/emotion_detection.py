import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 200:        
        result = json.loads(response.text)
        dominant_emotion = ''
        dominant_value = 0.0000
        emotion_predictions = result['emotionPredictions'][0]
        emotions = emotion_predictions['emotion']
        for key, value in emotions.items():
            if float(value) > float(dominant_value):
                dominant_value = value
                dominant_emotion = key

        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None,}

