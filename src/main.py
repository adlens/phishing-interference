from generator import load_credentials
from submitter import submit_fake_credentials


def main():
    url = "https://findmy-device-account.com/Uk"
    file_path = "data/credentials.json"
    credentials = load_credentials(file_path)
    print(credentials)
    submit_fake_credentials(url, credentials)


if __name__ == "__main__":
    main()
