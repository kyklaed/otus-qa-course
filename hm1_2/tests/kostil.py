import subprocess
import argparse


def start_test(args):
    if args.address == "https://api.cdnjs.com":
        sub = subprocess.Popen(["pytest", "-s", "-v", "cdnjs.py", "--address", args.address])
        sub.communicate()
    elif args.address == "https://api.openbrewerydb.org":
        sub = subprocess.Popen(["pytest", "-s", "-v", "openbrewerydb.py", "--address", args.address])
        sub.communicate()
    elif args.address == "https://dog.ceo":
        sub = subprocess.Popen(["pytest", "-s", "-v", "dog.py", "--address", args.address])
        sub.communicate()
    elif args.address == "all":
        url = {1: ("cdnjs.py", "https://api.cdnjs.com"),
               2: ("openbrewerydb.py", "https://api.openbrewerydb.org"),
               3: ("dog.py", "https://dog.ceo")}
        for adr in url.keys():
            sub = subprocess.Popen(["pytest", "-s", "-v", url[adr][0], "--address", url[adr][1]])
            sub.communicate()


def parse_args():
    parser = argparse.ArgumentParser(description='Web test')
    subparsers = parser.add_subparsers()
    parser_append = subparsers.add_parser('append', help='Append a url')
    parser_append.add_argument('address')
    parser_append.set_defaults(func=start_test)
    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

main()
