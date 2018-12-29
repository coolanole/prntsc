# prntsc
Script for automatic downloading of unprotected user screenshots from [prnt.sc](https://prnt.sc)

## Installing
Do you need to install [pip](https://pypi.org/project/pip/)?
```bash
# To install pip, securely download get-pip.py.
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Then run the following:
$ python get-pip.py
```

Install from source with:
```bash
$ git clone https://github.com/coolanole/prntsc.git
$ cd prntsc
$ pip install
```

## Getting started
To run this script, Python 2.7 or later must be installed on your computer.
```bash
$ python app.py
```

## Work with a proxy
The script supports work through a proxy. To do this, create a file with a list of your proxies and run the script passing the path to the file as an argument. Each proxy server must be written with a new line.
```bash
$ python app.py --proxy proxy.txt
```

## Contributing
Contributions of all sizes are welcome, you can also help by [reporting bugs](https://github.com/coolanole/prntsc/issues).