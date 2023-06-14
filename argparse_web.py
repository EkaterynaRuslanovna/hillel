import argparse

parser = argparse.ArgumentParser(description="Site or PDF parsing for link validation")

parser.add_argument("--url", type=str, required=False, help="A URL argument, for example: http://www.google.com")
parser.add_argument("--pdf", type=str, required=False, help="The path to the PDF file, for example: 'src/links.pdf': ")

args = parser.parse_args()
