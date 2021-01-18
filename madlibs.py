"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/game')
def make_madlib():
    name = request.args.get("name")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adjective = request.args.get("adjective")

    return render_template("sentence.html",name=name,noun=noun,color=color,adjective =adjective)

@app.route('/play_game')
def show_madlib_form():
    """Give player option to play game."""

    # player = request.args.get("person")
    play_game = request.args.get("play_game")
    print(play_game)
    if play_game == "Yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")
    
        
       

@app.route('/compliment')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("player")
    play_game = request.args.get("play_game")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           player=player,
                           compliment=compliment)

@app.route("/sentence")
def show_madlib():
    """uses madlib choices to make a new sentence"""

    player = request.args.get("player")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adjective = request.args.get("adjective")

    return render_template("sentence.html", player=player,
                            noun=noun, color=color, adjective =adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
