from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load FAQ data
with open("faqs.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    faqs = data["college_faqs"]

# Smart chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check keywords
    for faq in faqs:
        for keyword in faq["keywords"]:
            if keyword in user_input:
                return faq["answer"]

    # Default reply
    return "Sorry, I can help with college info like fees, admission, courses, facilities, etc."

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

# Run app
if __name__ == "__main__":
    app.run(debug=True)