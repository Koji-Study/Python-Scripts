# ! -*- coding: utf-8 -*-
import pyttsx3

def voice():
    engine = pyttsx3.init()
    #设置语速
    engine.setProperty('rate', 130)
    #设置音量
    engine.setProperty('volume', 0.5)
    voices = engine.getProperty('voices')
    #设置第一个语音合成器
    engine.setProperty('voice', voices[0].id)
    for num in range(3):
        engine.say("新的运维事件产生，请及时处理")
    engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    voice()
