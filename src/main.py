from flask import Flask, request, render_template
from src.coordinator import CoordinatorAgent
from src.memory import Memory
import markdown

app = Flask(__name__, template_folder='../templates')
coordinator = CoordinatorAgent()
memory = Memory()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        # Basic input sanitization
        sanitized_query = query.strip() # Remove leading/trailing whitespace

        # For demonstration, using a fixed user_id. In a real app, this would be dynamic.
        user_id = "test_user"
        user_context = memory.get_user_context(user_id)
        user_context["query"] = sanitized_query

        response = coordinator.run(sanitized_query)

        # Convert Markdown response to HTML
        html_response = markdown.markdown(response)

        # Update memory with the latest interaction
        memory.set_user_context(user_id, {"last_query": sanitized_query, "last_response": response})
        memory.log({"user_id": user_id, "query": sanitized_query, "response": response})

        return render_template('index.html', query=sanitized_query, response=html_response)
    return render_template('index.html', query=None, response=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
