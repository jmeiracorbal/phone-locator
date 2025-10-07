# Phone Locator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![uv](https://img.shields.io/badge/uv-managed-blue.svg)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](https://github.com/jmeiracorbal/phone-locator)

A command-line tool to get detailed information about phone numbers. Discover location, carrier, timezone, and other details about any phone number.

## Features

- **Phone number analysis** - Get complete information about any phone number
- **Country and region detection** - Country, region, city, and coordinates
- **Carrier details** - Mobile operator and service provider info
- **Timezone identification** - Automatically finds the right timezone
- **Number validation** - Check if phone numbers are valid and possible
- **Format conversion** - International, national, E.164 formats
- **Clean interface** - Colored terminal output

## Installation

### Option 1: Install as command-line tool

Install directly from the repository:

```bash
pip install git+https://github.com/jmeiracorbal/phone-locator.git
```

Or clone and install locally:

```bash
git clone https://github.com/jmeiracorbal/phone-locator.git
cd phone-locator
pip install .
```

After installation, run from anywhere:

```bash
phone-locator
```

### Option 2: Download pre-built executable

1. Go to [Releases](https://github.com/jmeiracorbal/phone-locator/releases)
2. Download the executable for your platform:
   - **Linux**: `phone-locator` (binary)
   - **macOS**: `phone-locator` (binary)
   - **Windows**: `phone-locator.exe` (executable)
3. Run directly without installation

**Linux/macOS:**

```bash
chmod +x phone-locator
./phone-locator
```

**Windows:**

```cmd
phone-locator.exe
```

### Option 3: Run with uv (for development)

```bash
git clone https://github.com/jmeiracorbal/phone-locator.git
cd phone-locator
uv run python main.py
```

## Usage

After installation or running the executable, enter a country code and phone number to get detailed information including location, carrier, timezone, and validity.

## Requirements

- Python 3.8 or higher
- Internet connection (for carrier lookup)

## Data Source

This tool uses the `phonenumbers` library by Google to parse and validate phone numbers with comprehensive metadata.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Original author**: [HUNXBYTS](https://github.com/HUNXBYTS)
- **Modified by**: [jmeiracorbal](https://github.com/jmeiracorbal)
- **Based on**: Ghost Tracker tool

## Support

If you run into any issues or have questions:
- Create an issue on GitHub
- Check the [Releases](https://github.com/jmeiracorbal/phone-locator/releases) page for the latest version

---

**Note**: This tool is for educational and legitimate purposes. Respect privacy and use it responsibly.
