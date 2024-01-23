from flask import Flask

app = Flask(__name__)
counter = 0

@app.route('/', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return f"Counter incremented. Total POST requests: {counter}"

@app.route('/', methods=['GET'])
def display_counter():
    return f"""
    <html>
        <head>
            <title>Counter Service</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f7f7f7;
                    text-align: center;
                    padding-top: 50px;
                }}
                .counter {{
                    font-size: 3em;
                    color: #5c5c5c;
                    margin: 20px;
                }}
                .content {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    display: inline-block;
                }}
            </style>
        </head>
        <body>
            <div class="content">
                <div class="counter">Total POST Requests: {counter}</div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8082)

