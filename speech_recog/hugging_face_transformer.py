import speech_recognition as sr
from transformers import pipeline

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="zh-TW")
        print("你说了: " + text)
        return text
    except sr.UnknownValueError:
        print("无法识别语音")
    except sr.RequestError as e:
        print("请求错误; {0}".format(e))
    return ""

def analyze_sentiment(text):
    # 使用Hugging Face的情感分析模型
    sentiment_pipeline = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")
    result = sentiment_pipeline(text)
    return result[0]['label']

if __name__ == "__main__":
    text = recognize_speech()
    if text:
        if "麥當勞" in text:
            print("检测到麥當勞关键词")
        sentiment = analyze_sentiment(text)
        print("情感分析结果: " + sentiment)
