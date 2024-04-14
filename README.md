# TAPO POST method adapter

This adapter is used to send POST requests to a given URL.
It can be used in conjunction with a Google TV remote and [Button Mapper](https://play.google.com/store/apps/details?id=flar2.homebutton) to send POST requests to a URL when a button is pressed. (HTTP POST request under Advanced)

## Installation

Install the requirements (listed [below](#requirements)), then clone this repository. Run the following command in the root directory of the repository:

```bash
git clone https://github.com/lucasburlingham/tapo-post-adapter.git
make install
```

This starts a PHP server on port 8000. You can now send POST requests to `http://localhost:8000`:

```bash
curl -X POST http://localhost:8000 -d q=toggle
```

to toggle the state of the lightbulb. You will need to replace the URL in the `index.php` file with the URL of the device you want to control, or use [`cloudflared`](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) to tunnel the requests to a local device.

Additionally, you need to add the username and password to your TP-Link account to the credentials.env file. The file should look like this:

```bash
johndoe@example.com
password123
```

The file is automatically created and looks like the above snippet when you run `make devserver` for the first time.

## Uninstallation

To stop the server, run the following command in the root directory of the repository:

```bash
make uninstall
```

## Requirements

- PHP
- Make
- python3 & pip
- [cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) (optional)
- [Button Mapper](https://play.google.com/store/apps/details?id=flar2.homebutton) (optional)

## Testing

**"It doesn't even work on my machine."**

My dev environment:
Ubuntu 23.10 with Python 3.11.6, PHP 8.2.10-2ubuntu1, curl 8.2.1, cloudflared 2022.4.0, and GNU Make 4.3.

Deployed on:
[RPI 0 W (32-bit)](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) version 1 from 2017

To control: [TP-Link TAPO L530E](https://www.amazon.com/dp/B0B2KWJLZT)

## Contributing

Please open an issue if you have any questions or suggestions. I won't be doing pull requests for this project, as it is a personal project and quite niche.

## Special Thanks

[@Cosik](https://github.com/Cosik/TapoP100) for his fork of [@fishbigger](https://github.com/fishbigger/TapoP100)'s TapoP100, which inspired this project.
This fork was used because it added the ability to toggle the state of the Tapo plugs, which was not present in the original project. I don't use this functionality, but
would like to keep it in case I need it in the future.
