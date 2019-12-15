import PyPDF2 as pdf
from gtts import gTTS


    #taking in the pdf file and converting it to a word

pdfFileObject = open('test2.pdf','rb')
pdfReader = pdf.PdfFileReader(pdfFileObject)
pg = pdfReader.getNumPages()
print(pg)

finalDoc = ""

for i in range(0,pg):
    pageObj = pdfReader.getPage(i)
    finalDoc += (" " + pageObj.extractText().strip())

#converting text present in finalDoc to speech

#selecting the language
language = 'en'
myObj = gTTS(text = finalDoc, lang = language, slow = False)

myObj.save("testAudio.mp3")
