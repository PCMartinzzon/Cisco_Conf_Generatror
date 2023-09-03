<br/>
<p align="center">
  <a href="https://github.com/PCMartinzzon/Cisco_Conf_Generatror">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Cisco Configuration Generator</h3>

  <p align="center">
    <a href="https://github.com/PCMartinzzon/Cisco_Conf_Generatror/issues">Report Bug</a>
    .
    <a href="https://github.com/PCMartinzzon/Cisco_Conf_Generatror/issues">Request Feature</a>
  </p>
</p>

![Issues](https://img.shields.io/github/issues/PCMartinzzon/Cisco_Conf_Generatror) ![License](https://img.shields.io/github/license/PCMartinzzon/Cisco_Conf_Generatror) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

A simple CLI script to speed up Base configuration for Cisco Routers and Switches.

Commands available now:
* Enable
* Configure terminal
* Hostname
* No domain lookup (preventing domain lookups, resulting in having to wait for X amount of seconds before you can continue configuring)
* Configuring console lines
* Configuring VTY lines (for remote control)
* Password for IOS
* Password for console line
* Password for the vty line
* Whether you want to configure a switch (both layer 2 and layer 3 are supported) or router
* (Ranges of) interfaces (automatically does a no shutdown after setting an IP-address as well)
* IP-addresses
* Subnetmasks
* Description for interfaces
* Username for SSH access
* Password for SSH access
* Domain names
* SSH and generating 2048-bit RSA keys
* Password encryption
* Banner MOTD (Message Of The Day)
* Routing (OSPF)
* Static routes
* VLAN IDs
* Putting VLANs in either trunk or access mode
* IP-routing
* Copying the running config to the startup config (with a do write)

## Built With

Python 3.11

## Getting Started

TBD

### Prerequisites

TBD

### Installation

TBD

## Usage

TBD

## Roadmap

Commands to add:
* EIGRP
* BGP
* Port-Channel (PAGP/LACP)
* Advance user creator
* STP

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/PCMartinzzon/Cisco_Conf_Generatror/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/PCMartinzzon/Cisco_Conf_Generatror/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

LGPL-3.0 license

## Authors

* **Patrik Martinsson** - *Research Assistant - Network security* - [Patrik Martinsson](https://github.com/PCMartinzzon/)

## Acknowledgements

* [AnonymousWP](https://github.com/AnonymousWP/)
