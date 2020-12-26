#render_template is used to render the html file in template folder,request is used to request data from html &
#vice versa,url_for is used to display logic from flask in html file
from flask import Flask, render_template, request, url_for 
from flask_bootstrap import Bootstrap
#used to divide the words
from textblob import TextBlob,Word
#used in nlp applications
import random
#used to show much timec it takes
import time


#every flask app will start with this
app=Flask(__name__)

#bootstrap app
Bootstrap(app)

@app.route('/') #routing our logic which goes to html file,taking input
def index():
    return render_template('index.html')  #method specifies the file to be rendered

@app.route('/analyse',methods=['POST']) #analyse the input,POST is use for secure
def analyse():
    start=time.time()
    if request.method=='POST':
        rawtext=request.form['rawtext']
        blob=TextBlob(rawtext) #initialising the blob
        received_text=blob #storing input
        blob_sentiment,blob_subjectivity=blob.sentiment.polarity,blob.sentiment.subjectivity
        number_of_tokens=len(list(blob.words)) #number of words
        nouns=list()  #store list of nouns used in input 
        for word, tag in blob.tags:
            if tag=='NN': #if it is a noun
                nouns.append(word.lemmatize()) #capitalize the words
                len_of_words=len(nouns)
                rand_words=random.sample(nouns,len(nouns)) #catgorise which are not noun,eliminating unwanted words like article
                final_word=list()
                for item in rand_words:
                    word=Word(item).pluralize() #pluralize the words
                    final_word.append(word)
                    summary=final_word
                    end=time.time()
                    final_time=end-start



    return render_template('index.html',received_text=received_text, number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,
    blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time)

if __name__=='__main__':
    app.run(debug=True)
