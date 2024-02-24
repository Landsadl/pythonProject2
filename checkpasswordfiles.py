import requests
import hashlib
import sys
import logging


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an HTTPError for bad responses
        return res
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching: {e}')
        return None


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five)
    if response:
        return get_password_leak_count(response, tail)
    return 0


def check_passwords_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        return []

    return passwords


def main(file_path):
    passwords = check_passwords_from_file(file_path)

    if not passwords:
        print("No passwords found in the file.")
        return

    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should change the password.')
        else:
            print(f'{password} was NOT found. Great Password!')
    return 'done!'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/passwords.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    sys.exit(main(file_path))
