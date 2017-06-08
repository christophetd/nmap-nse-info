# NSEInfo

NSEInfo is a tool to

# Sample usages

## Search

Find all NSE scripts related to NFS:

```
xxx search nfs
```

Find all NSE exploit scripts related to SMB:

```
xxx search smb --category exploit
```

Display all the NSE scripts in the category `brute` (bruteforce):

```
xxx --show-all --category brute
```

Show the first 5 NSE scripts in the category `discover`:

```
xxx --show-all --category discovery --limit 5
```

Display all the NSE scripts installed:

```
xxx --show-all
```

If your NSE scripts are not the standard location `/usr/share/nmap/scripts/`, you can use the `-l` or `--location` option to provide your customized path.

## Usage samples

Show a quick description and sample usages (if available) of the NSE script `http-wordpress-enum`:

```
xxx usage http-wordpress-enum
```
 
# Running the tests

```
$ python -m unittest discover test
```
