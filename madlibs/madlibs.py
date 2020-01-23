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


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():

    response = request.args.get("answer")

    if response == "no":

        return render_template("goodbye.html")

    return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")

    name = request.args.get("name")

    adjective = request.args.get("adjective")

    noun = request.args.get("noun")

 

    # if noun_2:
    #     noun_2 = request.args.get("noun_2")
    # else:
    #     noun_2 = "poopy"   

    choices = request.args.getlist("choice")
    print(request.args)
    print(choices)



    return render_template("madlib.html", color=color, name=name, adjective=adjective, noun=noun, choices = choices)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
