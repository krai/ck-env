# Turn an arbitrary bash script into a CK environment:

Installation (via detection) :
```
$ ck detect soft:load_bash_script --full_path=$HOME/CK/ck-env/soft/load_bash_script/print_hello.sh --extra_tags=greetings
```

Usage:
```
$ ck virtual env --tags=load,bash,greetings
```

Cleanup:
```
$ ck clean env --tags=source,load,bash,greetings
```
