from transformers import pipeline

# Use a smaller, faster summarization model
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")

def generate_summary(text):
    if len(text.split()) > 700:
        text = ' '.join(text.split()[:700])
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']
