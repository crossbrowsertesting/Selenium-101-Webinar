# CrossBrowserTesting 201 Webinar: Getting Started with Selenium

## Setup
To run the examples, you will need 
* Python 2.7
* Selenium module for Python

If you are juggling multiple versions of Python, check out [PyEnv](https://github.com/pyenv/pyenv). It makes it easy to install and manage multiple versions of Python on the same machine.

Once you have Python installed, you can install Selenium with pip:
```
pip install selenium
```

If you are running these examples from Windows or Linux you'll need to change the examples to point at the correct `chromedriver` for your system. For example, on Windows you would change the line

```
driver = webdriver.Chrome("./webdrivers/chromedriver")
```

to 

```
driver = webdriver.Chrome("./webdrivers/chromedriver.exe")
```

## Running the examples
Once everything is installed, running the examples is simple:
```
python 1-webdriver.py
```

## Questions? Comments? Problems?
If you encounter any issues or have any questions or suggestions, please open an issue in this repo and we'll get back to you.
