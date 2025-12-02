import json
import argparse
import funcy
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser(description='Splits COCO annotations file into training and test sets.')
parser.add_argument('annotations', metavar='coco_annotations', type=str,
                    help='Path to COCO annotations file.')
parser.add_argument('--train_ratio', type=float, dest='ratio_train', help='set train dataset ratio')
parser.add_argument('--valid_ratio', type=float,  dest='ratio_valid',help='set valid dataset ratio')
parser.add_argument('--test_ratio', type=float,  dest='ratio_test',help='set test dataset ratio')
parser.add_argument('--trainJson_name', type=str, default='train.json', help='Where to store COCO training annotations')
parser.add_argument('--validJson_name', type=str, default='valid.json', help='Where to store COCO valid annotations')
parser.add_argument('--testJson_name', type=str, default='test.json', help='Where to store COCO test annotations')
parser.add_argument('--annotations', dest='annotations', action='store_true',
                    help='Ignore all images without annotations. Keep only these with at least one annotation')

args = parser.parse_args()

ratio_train = args.ratio_train
ratio_valid = args.ratio_valid
ratio_test = args.ratio_test

def save_coco(file, images, annotations, categories):
    with open(file, 'wt', encoding='UTF-8') as coco:
        json.dump(
            {
                'images': images, 
                'annotations': annotations, 
                'categories': categories
            }, coco, indent=2, sort_keys=True
        )

def filter_annotations(annotations, images):
    image_ids = funcy.lmap(lambda i: int(i['id']), images)
    return funcy.lfilter(lambda a: int(a['image_id']) in image_ids, annotations)

def main(args):
    with open(args.annotations, 'rt', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        images = coco['images']
        annotations = coco['annotations']
        categories = coco['categories']

        images_with_annotations = funcy.lmap(lambda a: int(a['image_id']), annotations)

        if args.annotations:
            images = funcy.lremove(lambda i: i['id'] not in images_with_annotations, images)

        train_before, test = train_test_split(
            images, test_size=ratio_test)

        ratio_remaining = 1 - ratio_test
        ratio_valid_adjusted = ratio_valid / ratio_remaining

        train_after, valid = train_test_split(
            train_before, test_size=ratio_valid_adjusted)

        save_coco(args.trainJson_name, train_after, filter_annotations(annotations, train_after), categories)
        save_coco(args.testJson_name, test, filter_annotations(annotations, test), categories)
        save_coco(args.validJson_name, valid, filter_annotations(annotations, valid), categories)

        print("Saved {} entries in {} and {} in {} and {} in {}".format(len(train_after), args.trainJson_name, len(test), args.testJson_name, len(valid), args.validJson_name))


if __name__ == "__main__":
    main(args)
