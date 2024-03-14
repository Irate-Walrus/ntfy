# NTFY

I really liked ntfy.sh but didn't like the fact it was unecrypted.

```
Usage: ntfy [OPTIONS]

  Send notification to Telegram channel.

Options:
  --title TEXT  Title for the notification
  --text TEXT   Text for the notification
  --channels    List joined Telegram channels
  --help        Show this message and exit.
```

## Installation & Setup

1. Clone the repository.
2. Build the application: `poetry build`
3. Install the application: `pipx install dist/ntfy-0.1.0.tar.gz`
4. Create a config directory:
     - Linux: `~/.config/ntfy'
     - Windows `~/AppData/Roaming/ntfy`
5. Copy-Paste the following into the config directory as `config.toml` and add your bot details:

```toml
[telegram]
api_id = YOUR-API-ID
api_hash = YOUR-API-HASH
channel_id = YOUR-PRIVATE-CHANNEL-ID
```
6. Execute `ntfy` and register session.
