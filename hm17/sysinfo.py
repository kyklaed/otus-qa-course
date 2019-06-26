import subprocess
import argparse


def inform(args):
    if args.i == 1:
        with subprocess.Popen(["ip", "link"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.r == 2:
        with subprocess.Popen(["ip", "r"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.p == 3:
        with subprocess.Popen(["top", "-bn1"], stdout=subprocess.PIPE) as sub:
            print(sub.stdout.read().decode('utf-8').split('\n')[2])

    elif args.pi is not None:
        with subprocess.Popen(["ps", "--pid", args.pi], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.allp == 4:
        with subprocess.Popen(["ps", "-A"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.si == 5:
        with subprocess.Popen(["ip", "-s", "link"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.sinf is not "None" and args.sinf is not None:
        with subprocess.Popen(["service", args.sinf, "status"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.pinf is not None:
        with subprocess.Popen(["lsof", "-i", ":{0}".format(args.pinf)], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)

    elif args.pkginf is not "None" and args.pkginf is not None:
        try:
            with subprocess.Popen([args.pkginf, "--version"], stdout=subprocess.PIPE) as sub:
                for i in sub.stdout.read().decode('utf-8').split('\n'):
                    print(i)
        except Exception as err:
            print(err)

    elif args.fl is not "None" and args.fl is not None:
        try:
            with subprocess.Popen(["ls", args.fl], stdout=subprocess.PIPE) as sub:
                for i in sub.stdout.read().decode('utf-8').split('\n'):
                    print(i)
        except Exception as err:
            print(err)

    elif args.pwd == 7:
        with subprocess.Popen(["pwd"], stdout=subprocess.PIPE) as sub:
            print(sub.stdout.read().decode('utf-8'))

    elif args.core == 8:
        with subprocess.Popen(["uname", "-r"], stdout=subprocess.PIPE) as sub:
            print(sub.stdout.read().decode('utf-8'))

    elif args.opv == 9:
        with subprocess.Popen(["cat", "/etc/lsb-release"], stdout=subprocess.PIPE) as sub:
            for i in sub.stdout.read().decode('utf-8').split('\n'):
                print(i)


def parse_args():
    parser = argparse.ArgumentParser(description='System information')
    parser.add_argument('-i', nargs='?', const=1, type=int, help="Network interface")
    parser.add_argument('-r', nargs='?', const=2, type=int, help="Default route")
    parser.add_argument('-p', nargs='?', const=3, type=int, help="Information about the state of the processor")
    parser.add_argument('-pi', help="Process information")
    parser.add_argument('-allp', nargs='?', const=4, type=int, help="List of all processes")
    parser.add_argument('-si', nargs='?', const=5, type=int, help="Network interface statistics")
    parser.add_argument('-sinf', nargs='?', const="None", type=str, help="Status of any service")
    parser.add_argument('-pinf', nargs='?', const=6, type=int, help="The status of the network port on a server (TCP or UDP)")
    parser.add_argument('-pkginf', nargs='?', const="None", type=str, help="Package version (the package name is passed as an argument)")
    parser.add_argument('-fl', nargs='?', const="None", type=str, help="The list of files in the directory")
    parser.add_argument('-pwd', nargs='?', const=7, type=int, help="The current directory")
    parser.add_argument('-core', nargs='?', const=8, type=int, help="Kernel version")
    parser.add_argument('-opv', nargs='?', const=9, type=int, help="Operating system version")
    parser.set_defaults(func=inform)
    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

main()
