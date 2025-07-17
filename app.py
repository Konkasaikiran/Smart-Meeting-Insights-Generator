from flask import Flask, render_template, request
from summarizer import generate_summary
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    transcript = request.form['transcript']
    summary = generate_summary(transcript)
    sentiment = analyze_sentiment(transcript)
    return render_template('result.html', summary=summary, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
from flask import make_response
from xhtml2pdf import pisa
from io import BytesIO

@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    summary = request.form['summary']
    sentiment = request.form['sentiment']

    html = render_template('pdf_template.html', summary=summary, sentiment=sentiment)
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result)

    if pisa_status.err:
        return "PDF generation error", 500

    response = make_response(result.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=meeting_summary.pdf'
    response.headers['Content-Type'] = 'application/pdf'
    return response
