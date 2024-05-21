# Phishing Interference Project

## Purpose

The purpose of this project is to disrupt phishing operations by submitting large amounts of fake data to phishing websites, thereby protecting users' privacy and security.

## Story

A friend of mine had her phone stolen, and the thief, unable to unlock it, resorted to a new trick. The thief sent a link (https://findmy-device-account.com/Uk), which mimics Apple's official "Find My Device" page. The unsuspecting victim is prompted to enter their Apple ID and password, only to be told their credentials are incorrect. Meanwhile, the thief is actually harvesting these credentials in the background, hoping to use them to unlock the stolen phone.

To thwart these malicious efforts, I decided to write a Python program using Selenium to flood this phishing site with a barrage of fake email and password combinations. The idea is to obscure any real data the thief might collect, making it significantly harder for them to unlock stolen devices. Additionally, this will increase their database load and operational costs, hopefully discouraging them from continuing their scam.

## Usage

### Step 1: Clone the Project Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/adlens/phishing-interference.git
```

### Step 2: Install Dependencies

Install Pipenv if you haven't already:

```bash
pip install pipenv
```

Navigate to the project directory and install dependencies:

```bash
pipenv install
```

### Step 3: Generate Fake Credentials

Use Mockaroo or a similar website to generate a JSON file with fake email and password data. For example, you can create a schema on [Mockaroo](https://mockaroo.com/) with the following fields:

- `email`: Use the "Email Address" type.
- `password`: Use the "Password" type.

Download the generated data as `credentials.json` and place it in the `data/` folder of the project.

### Step 4: Ensure Firefox and Geckodriver are Installed

Make sure you have Firefox installed on your machine. Download and install Geckodriver from the [Geckodriver releases page](https://github.com/mozilla/geckodriver/releases) and ensure it's in your system PATH.

### Step 5: Run the Program

Run the program to start submitting fake credentials to the phishing site:

```bash
pipenv run python src/main.py
```

## Disclaimer

- This project is intended for educational and research purposes only and should not be used for illegal activities.
- Use headless browser mode to reduce system resource consumption.
- Implement appropriate delays and error handling to avoid IP blocking due to frequent requests.
