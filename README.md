
## ※※※ Base code ※※※
https://github.com/akarazniewicz/cocosplit / akarazniewicz 
(coco, train, test split)

- In the existing code, just edit parser, save line and add ratio calculate code


# coco-split_train_test_valid
If you want to separate the [train, test] sets, use the base code,
and you want to separate the [train, valid, test] sets, use this code.


## init enviornment
pip install -r requirments


## How to use?
$ python coco-split_train_test_valid.py \
--annotations {annotationsFile, only Json} \
--train_ratio {own train_ratio} \
--valid_ratio {own valid_ratio} \
--test_ratio {own test_ratio} \
--trainJson_name {save fileName, Has a default} \
--validJson_name {save fileName, Has a default} \
--testJson_name {save fileName, Has a default}


## Option information
$ python coco-split_train_test_valid.py -h
