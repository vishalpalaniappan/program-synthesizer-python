import sys
import argparse

def main(argv):

    args_parser = argparse.ArgumentParser(
        description="Synthesizes a python program given the package with the metadata"
    )

    args_parser.add_argument(
        "--package",
        required=True,
        help="Path to synth package json file"
    )
    
    parsed_args = args_parser.parse_args(argv[1:])
    package = parsed_args.package

    try:
        open(package)
    except Exception as e:
        print(f"Invalid arguments: {str(e)}", file=sys.stderr)
        return -1

    print(package)


if "__main__" == __name__:
    sys.exit(main(sys.argv))