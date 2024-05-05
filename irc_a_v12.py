import irc.client
import irc.schedule
import sys
import os
from dotenv import load_dotenv
from voice import dubbing
load_dotenv()

def on_connect(connection, event):
    channel = os.getenv('CHANNEL')
    channel = '#' + channel
    connection.join(channel)
    print(f'connected to the {channel}')

def on_join(connection, event):
    print(f'Joined {event.target}')

def on_publicmsg(connection, event):
    print(f'Message from {event.source.nick}: {event.arguments[0]}')
    dubbing(event.arguments[0])

def on_disconnect(connection, event):
    print('Disconnected, Reconnecting...')
    connect_to_twitch()

def connect_to_twitch():
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = os.getenv('CHANNEL')
    passowrd = os.getenv('OAUTH')

    reactor = irc.client.Reactor()
    try:
        conncetion = reactor.server().connect(server, port, nickname, passowrd)
    except irc.client.ServerConnectionError:
        print(sys.exc_info()[1])
        raise SystemExit
    conncetion.add_global_handler('welcome', on_connect)
    conncetion.add_global_handler('join', on_join)
    conncetion.add_global_handler('pubmsg', on_publicmsg)
    conncetion.add_global_handler('disconnect', on_disconnect)
    reactor.process_forever()


if __name__ == '__main__':
    connect_to_twitch()


