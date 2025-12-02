
## ※※※ Base code ※※※
https://github.com/akarazniewicz/cocosplit / akarazniewicz 
(coco, train, test split)

- In the existing code, just edit parser, save line and add ratio calculate code


# cocosplit_train_test_valid
If you want to separate the [train, test] sets, use the base code,
and you want to separate the [train, valid, test] sets, use this code.

## init enviornment
pip install -r requirements.txt


## How to use?
```bash
python cocosplit_train_test_valid.py \\  
--annotations {annotationsFile, only Json} \\  
--train_ratio {own train_ratio} \\  
--valid_ratio {own valid_ratio} \\  
--test_ratio {own test_ratio} \\  
--trainJson_name {save fileName, Has a default} \\  
--validJson_name {save fileName, Has a default} \\  
--testJson_name {save fileName, Has a default}
```

## example
```bash
python cocosplit_train_test_valid.py \\  
--annotations ./target.json \\  // input your target json file path  
--train_ratio 0.8 \\  
--valid_ratio 0.1 \\  
--test_ratio 0.1 \\  
--trainJson_name train.json \\  
--validJson_name valid.json \\  
--testJson_name test.json 
```

## what is 'cocosplit_train_test_valid.py' and 'cocosplit_train_test_valid_fileVer.py'
'cocosplit_train_test_valid.py' version is just split json file to train, test, valid file  
'cocosplit_train_test_valid_fileVer.py' version is split json file and copy real files to json path

## Option information
```bash
python cocosplit_train_test_valid.py -h
```
