import irc.client
import irc.schedule
import sys
import pyttsx3

#Setting up a pyttsx3:
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices: #Available voices 
    print(voice)
engine.setProperty('voice', voices[0].id) # Setting the voice 

#Irc setting up 

#Who connected to the chat
def on_connect(connection, even):
    channel = 'Channel name, example: #html_is_a_programming_lang'
    connection.join(channel)
    print(f'Connected to the {channel}')

def on_join(connection, event):
    print(f'Joined {event.target}')

#What writes 
def on_publicmsg(connection, event):
    print(f'Message from {event.source.nick}: {event.arguments[0]}')
    chat_message = event.arguments[0]
    print(chat_message)
    #dubbing the message 
    engine.say(chat_message)
    engine.runAndWait()

#Reconnecting 
def on_disconnect(connection, event):
    print('Disconnected, Reconnecting...')
    connect_to_twtich()

#Ports 
def connect_to_twtich():
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'Your nickname'
    password = '#Oauth token, example: oauth:fjru0284tw0hg'

    reactor = irc.client.Reactor()
    try:
        connection = reactor.server().connect(server, port, nickname, password=password)
    except irc.client.ServerConnectionError:
        print(sys.exc_info()[1])
        raise SystemExit
    connection.add_global_handler('welcome', on_connect)
    connection.add_global_handler('join', on_join)
    connection.add_global_handler('pubmsg', on_publicmsg)
    connection.add_global_handler('disconnect', on_disconnect)
    
    reactor.process_forever()

if __name__ == '__main__':
    connect_to_twtich()

