from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/', methods=['POST'])
def increment_counter():
    # Increment the counter in Redis
    counter = redis_client.incr('counter')
    return f"Counter incremented. Total POST requests: {counter}"

@app.route('/', methods=['GET'])
def display_counter():
    # Retrieve the counter value from Redis
    counter = redis_client.get('counter') or 0
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
                <div class="counter">Total POST Requests: {str(counter)}</div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8080)
