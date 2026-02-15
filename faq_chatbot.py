import sys
import time
import re
sys.stdout.reconfigure(encoding='utf-8')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# -------------------------------
# FAQ DATASET (Online Shopping)
# -------------------------------

faq_questions = [
    "How can I track my order?",
    "What is the return policy?",
    "How do I cancel my order?",
    "Do you offer cash on delivery?",
    "How long does delivery take?",
    "How can I contact customer support?",
    "Are there any delivery charges?",
    "Can I change my delivery address?"
]

faq_answers = [
    "You can track your order from the 'My Orders' section.",
    "Our return policy allows returns within 7 days of delivery.",
    "Go to My Orders and select cancel order.",
    "Yes, we offer cash on delivery in selected locations.",
    "Delivery usually takes 3-5 business days.",
    "You can contact support via email or helpline number.",
    "Delivery is free for orders above ₹499.",
    "Yes, you can change the address before the order is shipped."
]

# -------------------------------
# NLP MODEL
# -------------------------------

vectorizer = TfidfVectorizer(
    preprocessor=clean_text,
    stop_words='english',
    ngram_range=(1, 2)
)
faq_vectors = vectorizer.fit_transform(faq_questions)

def bot_typing(text):
    print("Bot: ", end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

# -------------------------------
# CHAT FUNCTION
# -------------------------------

def get_best_answer(user_question):
    user_vec = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vec, faq_vectors)
    index = similarity.argmax()
    score = similarity[0, index]

    if score < 0.3:
        return "Sorry, I couldn't understand your question."
    confidence = round(score * 100, 2)
    answer = faq_answers[index]

    return f"{answer} (confidence: {confidence}%)"

# -------------------------------
# CHAT LOOP
# -------------------------------

print("🛒 Online Shopping FAQ Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you! Happy shopping! 👋")
        break

    response = get_best_answer(user_input)
    print("Bot:", response)
