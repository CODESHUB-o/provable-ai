import argparse
import sys

from tools.offline_verify import verify_proof


def main():

    parser = argparse.ArgumentParser(
        prog="provable-ai",
        description="Provable AI verification CLI"
    )

    sub = parser.add_subparsers(dest="command")

    verify_cmd = sub.add_parser(
        "verify",
        help="Verify proof package"
    )

    verify_cmd.add_argument(
        "proof_file",
        help="Path to proof JSON"
    )

    args = parser.parse_args()

    if args.command == "verify":

        valid, message, state = verify_proof(args.proof_file)

        if valid:
            print("VALID:", message)
            if state:
                print("Final state:", state)
            sys.exit(0)

        else:
            print("INVALID:", message)
            sys.exit(1)

    parser.print_help()


if __name__ == "__main__":
    main()