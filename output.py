from flask import Flask, render_template_stringimport threadingapp = Flask(__name__)html_code = """<!DOCTYPE html><html><head>    <title>HTML Output</title></head><body>    <h1>Hello, World!</h1>    <p>This is HTML output generated by the assistant.</p></body></html>"""def run_flask():    app.run(debug=False)if __name__ == "__main__":    if "show me the output" in user_input:        # Start Flask in a separate thread to serve HTML content        threading.Thread(target=run_flask).start()        # Open a web browser to display the HTML content        import webbrowser        webbrowser.open("http://127.0.0.1:5000/")