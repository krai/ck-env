# A generic soft entry that simplifies creation of any environments

The main parameters are:

* `--full_path` *this is our anchor file*
* `--cus.anchor_depth` *how deep is the anchor (how many steps to float up from there*
* `--cus.env_prefix` *you will want to change this for each "type" of your entries, to avoid them from mutually excluding each other*
* `--cus.version` *finally! you can override this field as well*
* `--ienv._ANY_NAME` *starts with one underscore: will get promoted into the env_prefix domain without value change*
* `--ienv.__ANY_RELATIVE_PATH` *starts with double underscore: the resolved absolute path will get promoted into the env_prefix*

Usage example:
```
$ ck detect soft:generic.file.container --full_path=$HOME/location/for/visual/models --cus.anchor_depth=0 --cus.env_prefix=CK_ENV_VISUAL_MODELS --cus.version=visual_models --ienv.__ONNX_MODEL_PATH=visual/mobilenet/mobilenet.onnx --ienv._MODEL_WIDTH=224
```
