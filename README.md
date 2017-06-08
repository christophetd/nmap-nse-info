# NSEInfo

NSEInfo is a tool to interactively search through nmap's NSE scripts.

![screenshot](https://user-images.githubusercontent.com/136675/26920178-6affd926-4c38-11e7-9a4a-1fef0ea7d8f9.png)

![screenshot2](https://user-images.githubusercontent.com/136675/26920121-2ec1a9b2-4c38-11e7-8d06-54b1a1f3030f.png)


# Installation

Needs Python 2.7. To install, run:

```
pip install git+https://github.com/christophetd/nmap-nse-info.git
```

# Sample usages

## Search

Find all NSE scripts related to NFS:

```
nseinfo search nfs
```

Find all NSE exploit scripts related to SMB:

```
nseinfo search smb --category exploit
```

Display all the NSE scripts in the category `brute` (bruteforce):

```
nseinfo --show-all --category brute
```

Show the first 5 NSE scripts in the category `discover`:

```
nseinfo --show-all --category discovery --limit 5
```

Display all the NSE scripts installed:

```
nseinfo --show-all
```

If your NSE scripts are not the standard location `/usr/share/nmap/scripts/`, you can use the `-l` or `--location` option to provide your customized path.

## Usage samples

Show a quick description and sample usages (if available) of the NSE script `http-wordpress-enum`:

```
nseinfo usage http-wordpress-enum
```
 
## Running the tests

```
python -m unittest discover test
```
