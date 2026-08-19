# Interactive Python QR Code Generator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight CLI tool built with Python to convert custom text or URLs into high-density QR code images.

## Features
- **Interactive Prompts:** Dynamic user input for text/URLs and custom filenames.
- **High Error Correction (`ERROR_CORRECT_H`):** Up to ~30% data restoration for optimal scan reliability.
- **Auto-Formatting:** Ensures output defaults to valid `.png` file structures.

## 🛠️ Quick Start

```bash
# Clone the repository
git clone [https://github.com/manishbollikonda-318/QR-Generator.git](https://github.com/manishbollikonda-318/QR-Generator.git)

# Navigate to project directory
cd QR-Generator

# Install dependencies
pip install qrcode pillow

# Run the app
python generate_qr.py