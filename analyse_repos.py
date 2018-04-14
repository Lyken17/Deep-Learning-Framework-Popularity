import os, sys
import os.path as osp
import subprocess
import shutil
from pprint import pprint

# import git
# from git import Repo



frameworks = (
    "torch",
    "tensorflow",
    "mxnet",
    "theano",
    "keras",
    "matlab"
)


def find_keywords(path, word_bag):
    with open(path, "r") as fp:
        lines = fp.readlines()

    res = []
    for l in lines:
        for w in word_bag.keys():
            if w in l:
                res.append(w)
    res = list(set(res))
    return res


def analyse_one_repo(folder):
    word_bag = {_: False for _ in frameworks}
    word_count = {_: False for _ in frameworks}

    for (dirpath, dirnames, filenames) in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.py') and len(word_bag) > 0:
                # print(dirpath, filename)
                res = find_keywords(osp.join(dirpath, filename), word_bag)
                for key in res:
                    word_count[key] = True
                    del (word_bag[key])

            if filename.endswith('.m'):
                word_count["matlab"] = True

    return word_count


root = "test"
proj = "3D-ResNets-PyTorch"

for (dirpath, dirnames, filenames) in os.walk(root):
    break

word_count = {_: 0 for _ in frameworks}
for idx, proj in enumerate(dirnames):
    folder = osp.join(root, proj)
    w = analyse_one_repo(folder)
    pprint(folder)
    pprint(w)

    for key, value in w.items():
        if value == True:
            word_count[key] += 1

    print(word_count)
