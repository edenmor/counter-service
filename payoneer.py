from flask import Flask
import redis
import os

app = Flask(__name__)
# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')  # Default to 'localhost' if not set
redis_port = int(os.getenv('REDIS_PORT', 6379))    # Default to 6379 if not set

# Configure Redis connection
r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Initialize counter if not already set
if not r.exists('counter'):
    r.set('counter', 0)
@app.route('/reset', methods=['POST'])
def reset_counter():
    r.set('counter', 0)
    return "Counter has been reset."
if not r.exists('counter'):
    r.set('counter', 0)
@app.route('/one', methods=['POST'])
def reset1_counter():
    r.set('counter', 1)
    return "Counter has been set to 1."
@app.route('/two', methods=['POST'])
def reset2_counter():
    r.set('counter', 2)
    return "Counter has been set to 2."
@app.route('/', methods=['POST'])
def increment_counter():
    # Increment the counter in Redis
    counter = r.incr('counter')
    return f"Counter incremented. Total POST requests: {counter}"

@app.route('/', methods=['GET'])
def display_counter():
    # Retrieve the counter from Redis
    counter = r.get('counter').decode('utf-8')
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
    app.run(debug=True, port=8080)
