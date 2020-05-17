# lms notifier

A simple tool to keep track of your [Kharazmi lms](http://lms.khu.ac.ir/) courses

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You must have Python 3, Git and Google Chrome/Chromium on your machine
Windows users: [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/download/win), [Chrome](https://www.google.com/chrome/)
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
The first running of this file will create multiple files in the sources folder, further runnings will compare and extract changes from your lms account

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Pull requests are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details