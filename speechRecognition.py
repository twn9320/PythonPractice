# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:36:17 2021

@author: Jordan
"""
from gtts import gTTS #text to speech via google
from pygame import mixer # 說出聲音
import speech_recognition #speech to text
import tempfile #麥克風收音

#接收聲音
def listener():
  r = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as source:
      print("請說:")
      a = r.listen(source)
      return r.recognize_google(a,language="zh-TW")
#發出聲音    
def speaker(sentence):
  mixer.init()
  with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts = gTTS(text=sentence,lang="zh-tw")
    tts.save("{}.mp3".format(fp.name))
    mixer.music.load('{}.mp3'.format(fp.name))
    mixer.music.play()

#簡易問答
qa = {
  '天氣如何'  : '請自己去查',
  '誰在偷懶' : '凱凱正在偷懶',
  '你好嗎' :'還好'
  }
#speaker(qa.get(listener(),'對不起,我聽不懂'))

#查wiki百科
import requests
from bs4 import BeautifulSoup
def getWiki(keyword):
  res = requests.get("https://zh.wikipedia.org/wiki/{}".format(keyword))
  soup = BeautifulSoup(res.text,'lxml')
  article = soup.select_one(".mw-parser-output p").text
  return article

speaker(getWiki(listener()))