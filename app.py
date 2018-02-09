from flask import Flask #1

app = Flask(__name__) #2

@app.route('/')  #3
def home():
   return 'Hello, world!'

if __name__ == '__main__': #4
   app.run(debug=True)
