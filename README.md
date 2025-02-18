<div align="center">
  <img src="logo.png" alt="logo" width="200" height="auto" />
  <h1>Alerta Pisos</h1>
  
  <p>
    A bot that notifies you about new rental property listings.
  </p>
  
<h4>
    <a href="https://github.com/Ki-re/alerta-pisos/issues/">Report a bug</a>
  <span> · </span>
    <a href="https://github.com/Ki-re/alerta-pisos/issues/">Request a feature</a>
  <span> · </span>
    <a href="https://github.com/Ki-re/alerta-pisos/pulls">Contribute</a>
  </h4>
</div>

<br />

## Disclaimer

This script was designed in 2022 and is no longer being maintained. Feel free to adapt the code to your needs.

<!-- About the Project -->

## About the Project

This project is an automated bot that tracks rental property platforms and sends Telegram notifications with new available listings based on defined criteria.

<!-- Requirements -->

## Requirements

To run this project, you need to install the following dependencies:

```bash
pip install selenium
pip install requests
```

Additionally, you must download the chromedriver version that matches your Chrome version:

```bash
https://chromedriver.chromium.org/downloads
```

<!-- Configuration -->

## Configuration

Clone the repository:

```bash
git clone https://github.com/Ki-re/alerta-pisos.git
```

Create a Telegram bot with BotFather:

```bash
/newbot
```

Get your bot's token and the chat ID where you want to receive notifications:

```bash
telegram_bot_token = ""
chat_id = ""
```

Set up the `config.py` file with your search preferences and required credentials.

<!-- Usage -->

## Usage

Run the main script to start tracking rental properties:

```bash
python3 main.py
```

<!-- License -->

## License

Distributed under the no License. See LICENSE.txt for more information.
