# Discord Downloader

A Python script that downloads images and videos from a Discord channel. 

### Requirements

* Python 3.x
* Discord.py module

### Installation

1. Clone the repository or download `discord_downloader.py`.

2. Install the `discord.py` module via pip:

   ```
   pip install discord
   ```

3. Set your Discord bot token in the `TOKEN` variable inside the `discord_downloader.py` script.

### Usage

```
python3 discord_downloader.py <channel_id>
```

The script will create a folder with the channel name + id and download all images and videos from the channel into that folder.

When the script is finished running, it will print the total number of attachments downloaded.
