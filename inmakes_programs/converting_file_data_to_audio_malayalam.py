from gtts import gTTS
import os
text=open('demo.txt','r',encoding='utf=8').read()
language='ml'
output=gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp4')
os.system('start fileoutput.mp4')

