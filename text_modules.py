#1
def lines(text):
    '''This Function counts the number of lines in the given Text/Paragraph/Sentance'''
    return text.count("\n") + 1
#2
def sentences(text):
    '''This Function counts the number of sentences in the given Text/Paragraph/Sentance'''
    if text[-1] == ".":
        return len(text.split(".")) - 1
    else:
        return len(text.split("."))
#3
def words(text):
    '''This Function counts the number of words in the given Text/Paragraph/Sentance'''
    return len(text.split())
#4    
def tabs(text):
    '''This Function counts the number of tabs in the given Text/Paragraph/Sentance'''
    return text.count("\t")
#5
def spaces(sentence):
    '''
    This function counts number of spaces in the given Text/Paragraph/Sentance
    '''
    spaces = 0
    for char in sentence:
        if char == " ":
            spaces += 1
    return spaces
#6
def capital(paragraph):
    '''
    This function converts the given Text/Paragraph/Sentance to upper letters.
    '''
    sentenceList = []
    sentenceString = ''
    for letter in paragraph:
        sentenceList.append(letter.upper())
    for char in sentenceList:
        sentenceString += char
    return sentenceString 
#7
def small(paragraph):
    '''
    This function converts the given Text/Paragraph/Sentance to small letters.
    '''
    sentenceList = []
    sentenceString = ''
    for letter in paragraph:
        sentenceList.append(letter.lower())
    for char in sentenceList:
        sentenceString += char
    return sentenceString
#8
def punctuations(text):
    '''Punctuations removed from the Given Text/Paragraph/Sentance 
   '''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_text = text
    for punctuation in punctuations:
        cleaned_text = cleaned_text.replace(punctuation, "")
    return cleaned_text
