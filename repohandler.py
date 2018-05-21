import os
import tempfile
import sys
import hashlib
import time
from git import Repo, exc

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')


def clone_repo(git_url):
    repo_dir = os.path.join(tempfile.gettempdir(), 'repo')
    if os.path.exists(repo_dir):
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        repo_dir = os.path.join(repo_dir, hash.hexdigest())
    try:
        repo = Repo.clone_from(git_url, repo_dir)
        logger.info('The repository has been successfully cloned')
        return repo
    except exc.GitCommandError:
        logger.error("Couldn't reach the remote repository")
        sys.exit()
