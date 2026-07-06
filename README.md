# contestSubmissionArchive
Updating archive of past programming competitions I took part in and my submissions for them. This repository also includes some basic tools for setting up general contest code and archiving.

## Setup

Ensure that your computer has version Python 3.10 or higher installed. This is only to ensure the archiving scripts work as intended as this repository is intended to work for competitive programming with any language.

Fork this repository and delete the `archive` folder for personal use. To then use the contest template generator, replace `template.py` with your own template file in the `LIVE` folder, naming it `template.xyz` where `xyz` is the language extension. Once complete refer to [Usage](#usage) section for further instruction.

## Usage

### Repository Structure

Below is the simplified repository structure.

```
└── 📁contestSubmissionArchive
    └── 📁archive
        └── 📁livecontests
        └── 📁practice
    └── 📁LIVE
        └── 📁contest folder
        ├── coding template
        ├── build.py
        ├── archive.py
    ├── .gitignore
    ├── README.md
    ├── Makefile
    ├── LICENCE    
```

`archive` folder contains all archived contest code. The subfolder `livecontests` is for code actually done during a realtime competition whereas `practice` is more freeform practice code. When forking this repository for personal archival use, this entire should be deleted. `LIVE` folder contains `build.py` for creating the contest folder in which you will have several copies of the coding template setup for use in a live contest and `archive.py` for archiving the contest folder to a specified subfolder in `archive`. These scripts are most easily accessible via the `Makefile`.

### Makefile Commands

`make build PATH=contestname` -> Creates multiple copies of the coding template and stores in subfolder `LIVE/contestname`.

`make archive PATH=folderpath` -> Moves the `LIVE/contestname` subfolder to `archive/folderpath`.