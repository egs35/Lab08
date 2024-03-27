from flask import Flask, render_template

app = Flask(__name__)

# List of poems
poems = [
    "Poem 1: Roses are red, violets are blue...",
    "Poem 2: The road not taken...",
    "Poem 3: Do not go gentle into that good night...",
    # Add more poems as needed
]

@app.route('/')
def index():
    return render_template('index.html', poems=poems)

@app.route('/poem')
def show_poem():
    # For simplicity, this always returns the first poem from the list
    poem = poems[0]
    return render_template('poem.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)
