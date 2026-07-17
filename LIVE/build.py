import argparse
from pathlib import Path
import os
import shutil

def parse_arguments():
    """Setup argument parser for the file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--name",default = "archive/unsorted")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    if args.name == "archive/unsorted":
        print("No name specified for the created folder, defaulting to contestcode")
        args.name = "contestcode"
    contest_path = os.path.join("LIVE",args.name)
    os.makedirs(contest_path,exist_ok=True)
    templatefile = [file for file in Path("LIVE").iterdir() if "template" in file.name][0]
    template_suffix = Path(templatefile).suffix

    # Change these to whatever you want the filenames to be
    contest_filenames = ["a","b","c","d","e","f","g"]

    for c in contest_filenames:
        newfile_name = os.path.join(contest_path,c+template_suffix)
        shutil.copy(str(templatefile),str(newfile_name))