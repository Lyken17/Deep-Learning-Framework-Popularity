import os, sys
import os.path as osp
import subprocess
import shutil


# import git
# from git import Repo

def _download(git_url, folder_path):
    os.system("git clone %s %s" % (git_url, folder_path))


class GitRepo():
    root = "test"

    def __init__(self,
                 url="https://github.com/yunjey/StarGAN",
                 root="test"):
        self.url = url
        self.root = root

        self.repo_name = url.split("/")[-1]
        self.git_url = url + ".git"
        self.folder_path = osp.join(self.root, self.repo_name)

    def download(self, force=False):
        os.makedirs(self.root, exist_ok=True)
        if force and osp.exists(self.folder_path):
            shutil.rmtree(self.folder_path, ignore_errors=True)
        _download(self.git_url, self.folder_path)


if __name__ == "__main__":
    if True:
        with open("cvpr_lists.txt", "r+") as fp:
            lines = fp.readlines()

        for line in lines:
            line = line.strip()
            g = GitRepo(url=line)
            g.download(force=True)
            # g = GitRepo()
            # g.download()
