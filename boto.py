"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json, random


@route('/', method='GET')
def index():
    return template("chatbot.html") # this is the function that runs when we send a Get request to the server the return statement uses the template function from bottle to render the HTML page


@route("/chat", method='POST')# saving the user message what the post request sent me.
def chat():
    user_message = request.POST.get('msg')
    response_message, response_animation = message_means(user_message)[0], message_means(user_message)[1]
    return json.dumps({"animation": response_animation, "msg": response_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js') # this function serve the static files needed


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css') # this function serve the static files needed


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images') # this function serve the static files needed

def message_means(message):
    lowered_message = message.lower() #je mets tout en minuscule au cas ou on me met des majuscules.
    profanity = ['anus', 'arse', 'arsehole', 'ass', 'assbite', 'asscock', 'assface', 'assmonkey', 'asshole',
                 'asssucker',
                 'bampot', 'bastard', 'bitch', 'bitchass', 'bitches', 'bullshit', 'cliface', 'clitfuck', 'cock',
                 'cockass',
                 'cockbite', 'cockface', 'cockfucker', 'cockhead', 'cockmonkey', 'cocknose', 'cockshit', 'cockwaffle',
                 'coochy', 'cooter', 'cunnie', 'cunt', 'cuntass', 'dick', 'dick-sneeze', 'dicksneeze', 'dickbag',
                 'dickface', 'dickfuck', 'dickfucker', 'dickmilk', 'dicks', 'dumb ass', 'fag', 'fatass', 'fellatio',
                 'fuck',
                 'fuckass', 'fuckbag', 'fucked', 'fucker', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckin', 'fucking',
                 'fuckup', 'goddamn', 'jackass', 'motherfucker', 'motherfucking', 'negro', 'pecker', 'prick', 'pussies',
                 'pussy']

    good_mood = ['good','fine', 'great', 'well', 'amazing', 'happy', 'happiness', 'bless', 'blessed', 'glad', 'funny', 'pretty', 'best',
        'better', 'hot']

    negative_mood = ['abandonned','abused','accused','arrogant','afraid','sad', 'mean','cry', 'crying,' 'unwell', 'hurt', 'bad',
                     'hostile','impatient','indifferent','indignant','insecure','insolent','lethargic','nervous']

    hello_list = ["hello","coucou","bonjour","bonsoir","salut","wesh","good morning","hi","good evening","hey", "greetings", "hey man","what's up","what's new","how's it going", "how are you doing","what's going on","how's life","how are things" ]

    work_list =["dentist","statistician","orthodontist","developer","data scientist","pediatrician","computer system analyst","obstetrician","gynecologist","software developer"]

    late_list =["late" , "waiting" , "wait" ,"behind" ,"behind time","belated", "too late"]

    animals= ["dog" , "cat", "lion", "lynx", "fox", "bird", "bear" ,"monkey", "crocodilus", "camel", "duck", "rabbits", "hamsters", "guinea pigs", "ferrets"]

    for word in lowered_message.split():

        if word in profanity:
            return profanity_response()

        elif word in good_mood:
            return good_mood_response()

        elif word in negative_mood:
            return negative_mood_response()

        elif word in hello_list:
            return hello_user()

        elif word in work_list:
            return work_response()

        elif word in late_list:
            return late_response()

        elif word in animals:
            return animals_response()

    if lowered_message[0:3] == "i'm" or lowered_message[0:10] == "my name is":
        return my_message(lowered_message)

    else:
        return ("Nice :)",'ok')

def profanity_response():
    return ("You are not polite !!I don't want to talk with you", "afraid")

def good_mood_response():
    return ("Happy to hear such a positive mood", "dancing")

def negative_mood_response():
    return ("You should call your best friends or drink wine, it helps ! ", 'crying')

def hello_user():
    hello_chatbot =["Hello, I am Chatbot.How are you","Bonjour, Can I help you?","Hi babe, can I help you?"]
    bot_response = random.choice(hello_chatbot)
    return (bot_response, 'excited')

def work_response():
    return("Happy to hear that you have a job that pay well, challenge you, not too stressfull and have a good salary ! ",'money')

def late_response():
    return ("I'm always late because people stop me for autographs and say Hi", 'waiting')

def animals_response():
    return ("I wish I could have a pet", 'heartbroke')

def my_message(message):
    if message[0:3] == "i'm":
        user_name = message[3:]
        return ("Bonjour " + user_name + ", nice to meet you.", 'giggling')
    else:
        user_name = message[11:]
        return ("Hey " + user_name + ", nice to meet you.", 'dog')

def main():
    run(host='localhost', port=7000) # when running the file itself we're running the main function that sets up the server definitions

if __name__ == '__main__':
    main()