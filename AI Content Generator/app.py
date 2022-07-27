from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals()) #Done



@app.route('/product-description', methods=["GET", "POST"]) #Done
def productDescription():
    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed product description for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}":'.format(submission)
        
    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"]) #Done
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a detailed Job description for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Generate a tweet on the subject: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"]) #Done
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a cold email to potential cients about: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"]) #Done
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Generate an Ad copy for product: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"]) #Done
def businessPitch():

    if request.method == 'POST':
        submission = request.form['businessPitch']
        query = "Generate a business ideas pitch for: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"]) #Done 
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate Youtube Video topic ideas on: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"]) #Done
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Write a detailed Youtube Video description for the following topic: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('video-description.html', **locals())


@app.route('/paragraph-summary', methods=["GET", "POST"]) #Done
def paragraphSummary():

    if request.method == 'POST':
        submission = request.form['paragraphSummary']
        query = "Summarize this for a second-grade student: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('paragraph-summary.html', **locals())


@app.route('/keyword-extractor', methods=["GET", "POST"]) #Done
def keywordExtractor():

    if request.method == 'POST':
        submission = request.form['keywordExtractor']
        query = "Extract keywords from this text: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('keyword-extractor.html', **locals())


@app.route('/ai-sentence', methods=["GET", "POST"]) #Done
def aiSentence():

    if request.method == 'POST':
        submission = request.form['aiSentence']
        query = "Correct this to standard English: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('ai-sentence.html', **locals())


@app.route('/key-points', methods=["GET", "POST"]) #Done
def keyPoints():

    if request.method == 'POST':
        submission = request.form['keyPoints']
        query = "What are key points I should know when studying about: {}".format(submission)
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n','<br>')
        prompt = 'AI Suggestions for "{}" are:'.format(submission)

    return render_template('key-points.html', **locals())









if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
