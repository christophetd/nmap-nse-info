# NSEInfo

NSEInfo is a tool to interactively search through nmap's NSE scripts.

[![asciicast](https://asciinema.org/a/4av670luoetzj17y7oxho3juh.png)](https://asciinema.org/a/4av670luoetzj17y7oxho3juh)


# Installation

Needs Python 2.7. To install, run:

```
$ pip install nltk prettytable
$ pip install git+https://github.com/christophetd/nmap-nse-info.git
```

# Sample usages

## Search

Find all NSE scripts related to NFS:

```
$ nseinfo search nfs

3 matches found.

+---------------+----------------------------------------------------------+-----------------+
|  Script name  |                       Description                        |    Categories   |
+---------------+----------------------------------------------------------+-----------------+
|   nfs-statfs  | Retrieves disk space statistics and information from a   | discovery, safe |
|               |                    remote NFS share.                     |                 |
+---------------+----------------------------------------------------------+-----------------+
| nfs-showmount |    Shows NFS exports, like the showmount -e command.     | discovery, safe |
+---------------+----------------------------------------------------------+-----------------+
|     nfs-ls    | Attempts to get useful information about files from NFS  | discovery, safe |
|               |                         exports.                         |                 |
+---------------+----------------------------------------------------------+-----------------+

```

Find all NSE exploit scripts related to SMB:

```
$ nseinfo search smb --category exploit
```

Display all the NSE scripts in the category `brute` (bruteforce):

```
$ nseinfo --show-all --category brute
```

Show the first 5 NSE scripts in the category `discover`:

```
$ nseinfo --show-all --category discovery --limit 5
```

Display all the NSE scripts installed:

```
$ nseinfo --show-all
```

If your NSE scripts are not the standard location `/usr/share/nmap/scripts/`, you can use the `-l` or `--location` option to provide your customized path.

## Usage samples

Show a quick description and sample usages (if available) of the NSE script `http-wordpress-enum`:

```
$ nseinfo usage nfs-ls

nfs-ls: Attempts to get useful information about files from NFS exports.

2 sample usages found:

 nmap -p 111 --script=nfs-ls <target>
 nmap -sV --script=nfs-ls <target>

Run "nmap --script nfs-ls --help" for more information.
```
 
## Running the tests

```
python -m unittest discover test
```
