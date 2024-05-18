import irc.client
import irc.schedule
import sys
import os
from dotenv import load_dotenv
from voice import dubbing

# Load environment variables from a .env file
load_dotenv()

def on_connect(connection, event):
    """
    Called when the bot connects to the server.
    Joins the specified channel.
    """
    channel = os.getenv("CHANNEL")
    channel = "#" + channel
    connection.join(channel)
    print(f"Connected to the {channel}")

def on_join(connection, event):
    """
    Called when the bot joins a channel.
    """
    print(f"Joined {event.target}")

def on_publicmsg(connection, event):
    """
    Called when a public message is received in the channel.
    Prints the message and triggers the dubbing function.
    """
    print(f"Message from {event.source.nick}: {event.arguments[0]}")
    dubbing(event.arguments[0])

def on_disconnect(connection, event):
    """
    Called when the bot disconnects from the server.
    Attempts to reconnect.
    """
    print("Disconnected, Reconnecting...")
    connect_to_twitch()

def connect_to_twitch(tw_nickname=None, tw_oauth=None):
    """
    Connects to the Twitch IRC server using provided or environment variables.
    """
    server = "irc.chat.twitch.tv"
    port = 6667

    # Determine whether to use GUI inputs or environment variables
    nickname = tw_nickname
    password = tw_oauth

    reactor = irc.client.Reactor()

    try:
        # Establish connection to the server
        connection = reactor.server().connect(server, port, nickname, password)
    except irc.client.ServerConnectionError:
        print(sys.exc_info()[1])
        raise SystemExit

    # Set up handlers for various IRC events
    connection.add_global_handler("welcome", on_connect)
    connection.add_global_handler("join", on_join)
    connection.add_global_handler("pubmsg", on_publicmsg)
    connection.add_global_handler("disconnect", on_disconnect)

    # Start the IRC event loop
    reactor.process_forever()

if __name__ == "__main__":
    connect_to_twitch()
