from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), decode_responses=True)

@app.route('/')
def index():
    count = r.incr('hits')
    return f'Hello hatake my goat this page now has  {count} views.'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5004)

