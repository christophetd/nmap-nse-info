# NSEInfo

NSEInfo is a tool to interactively search through nmap's NSE scripts.

[![asciicast](https://asciinema.org/a/4av670luoetzj17y7oxho3juh.png)](https://asciinema.org/a/4av670luoetzj17y7oxho3juh)


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
