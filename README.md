# lms notifier

A simple tool to keep track of your [Kharazmi lms](http://lms.khu.ac.ir/) courses

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You must have Python 3, Git and Google Chrome/Chromium along with Chrome Driver on your machine.

Windows users: [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/download/win), [Chrome](https://www.google.com/chrome/), [Chrome Driver](https://chromedriver.chromium.org/downloads)

Linux & MacOS:

```
sudo apt-get install python3.8
sudo apt-get install git
sudo apt-get install chromium-browser
```
And the project libraries
```
pip install pathlib selenium difflib
```
### Cloning

```
git clone https://github.com/ArmanJR/lms-notifier.git
cd lms-notifier
```

## Running

First open main.py and edit *lms_username* & *lms_password* with your lms account, then run
```
python main.py
```
The first running of this file will create multiple files in the sources folder, further runnings will compare and extract changes from your lms account.

## Contributing

Pull requests are welcome.

## License

This project is licensed under the MIT License
