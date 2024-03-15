#!/usr/env/bin python

import click
import tomli
from os import path, environ, remove
from telethon import TelegramClient, sync

CONFIG_PATH = path.join(
    environ.get("APPDATA")
    or environ.get("XDG_CONFIG_HOME")
    or path.join(environ["HOME"], ".config"),
    "ntfy",
)

CONFIG_FILE = path.join(CONFIG_PATH, 'config.toml')
SESSION_FILE = path.join(CONFIG_PATH, 'ntfy.session')
TMP_SESSION_FILE = path.join(CONFIG_PATH, 'ntfy.tmp.session')

config = {}
with open(CONFIG_FILE, 'rb') as fp:
    config = tomli.load(fp)

def get_text(ctx, param, value):
    stdin_text = ""
    if not click.get_text_stream('stdin').isatty():
        stream = click.get_text_stream('stdin')

        for line in stream:
            print(line.strip())
            stdin_text += line

    if not value and stdin_text:
        return stdin_text.strip()
    else:
        return value

def list_channels():
    with TelegramClient(TMP_SESSION_FILE, config['telegram']['api_id'], config['telegram']['api_hash']) as client:
        print(' ---- ID ----\t ---- NAME ----')
        for channel in client.get_dialogs():
            if channel.is_channel:
                print(f'{channel.id}\t{channel.name}')
    remove(TMP_SESSION_FILE)
    return

@click.command()
@click.option('--title', default='New Ntfy!', help='Title for the notification', required=False)
@click.option('--text', callback=get_text, help='Text for the notification', required=False)
@click.option('--channels', help='List joined Telegram channels (requires additional privs)', is_flag=True)
def notify(title: str, text: str, channels: bool):
    "Send notification to Telegram channel."
    if channels:
        list_channels()
        return

    client = TelegramClient(SESSION_FILE, config['telegram']['api_id'], config['telegram']['api_hash']).start(bot_token=config['telegram']['bot_token'])
    channel = client.get_entity(config['telegram']['channel_id'])
    client.send_message(channel, f"**{title}**\n{text}")


if __name__ == '__main__':
    notify()




