import PyPDF2 as pdf
from gtts import gTTS

def p2a(openLoc, saveLoc):
    pdfFileObject = open(openLoc,'rb')
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

    myObj.save(saveLoc+".mp3")
