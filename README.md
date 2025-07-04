# Plex Snitch

Plex Snitch is a simple utility for pinging a specified URL, designed to be packaged as a standalone executable. It is ideal for use cases where you want to notify a remote service (such as deadmanssnitch.com) that your Plex Media Server is running.

## Insalling Dependencies

To install the necessary dependencies for Plex Snitch, you can use [Pipenv](https://pipenv.pypa.io/en/latest/). First, ensure you have Pipenv installed, then run the following command in your terminal:

```bash
pipen install --dev
```

## Packaging an Executable

To package Plex Snitch as a single-file executable, use [PyInstaller](https://www.pyinstaller.org/) via Pipenv:

```
pipenv run pyinstaller --onefile plex-snitch.py
```

This will generate an executable in the `dist/` directory.

## Configuration: `snitch.txt`

The resulting executable expects to find a file named `snitch.txt` in directory in which it is installed. This file should contain the URL that Plex Snitch will ping. Make sure to create and place `snitch.txt` next to the executable before running it.

**Example directory structure:**

```
dist/
  plex-snitch.exe
  snitch.txt
```

## Usage

1. Create a `snitch.txt` file containing the URL to ping (e.g. https://nosnch.in/your-unique-id).
2. Place `snitch.txt` in the same directory as the executable.
3. Run the executable:
   - On Windows: `./plex-snitch.exe`
   - On Linux/macOS: `./plex-snitch`

## License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
