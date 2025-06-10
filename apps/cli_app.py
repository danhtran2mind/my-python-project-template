import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for text processing",
        epilog="Example: python cli_app.py --uppercase 'hello world'"
    )
    parser.add_argument(
        "text",
        help="Input text to process"
    )
    parser.add_argument(
        "-u", "--uppercase",
        action="store_true",
        help="Convert text to uppercase"
    )
    parser.add_argument(
        "-l", "--lowercase",
        action="store_true",
        help="Convert text to lowercase"
    )
    parser.add_argument(
        "-c", "--count",
        action="store_true",
        help="Count characters in text"
    )
    return parser

def process_text(args):
    text = args.text
    result = text

    if args.uppercase:
        result = text.upper()
    elif args.lowercase:
        result = text.lower()
    elif args.count:
        result = f"Character count: {len(text)}"
    
    return result

def main():
    parser = setup_parser()
    args = parser.parse_args()
    result = process_text(args)
    print(result)

if __name__ == "__main__":
    main()