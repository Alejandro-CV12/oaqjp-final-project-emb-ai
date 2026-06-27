import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convierte el texto de Watson en un diccionario de Python
    formatted_response = json.loads(response.text)
    
    # Extrae solo la sección de las emociones
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Guarda las 5 emociones con sus puntuaciones
    emotions = {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness']
    }
    
    # Busca cuál de las 5 emociones tiene el número más alto
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Agrega la emoción ganadora al resultado final
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
