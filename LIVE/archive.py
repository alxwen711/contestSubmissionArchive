import argparse
from pathlib import Path
import os
import shutil

def parse_arguments():
    """Setup argument parser for the file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--path",default = "archive/unsorted")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    folders = [f.name for f in Path("LIVE").iterdir() if f.is_dir()]
    if len(folders) == 0:
        print("No contest folder found, aborting")
    else:
        contest_folder = os.path.join("LIVE",folders[0])
        print(f"First folder found is {contest_folder}, archiving this to {args.path}.")
        os.makedirs(args.path,exist_ok=True)
        for item in Path(contest_folder).iterdir():
            shutil.move(str(item), args.path)
        try:
            Path(contest_folder).rmdir()
            print(f"{contest_folder} has been successfully removed.")
        except OSError:
            print(f"{contest_folder} still contains files and is not deleted.")