import os
def get_config():
    config = {
        'git_token': os.getenv('GIT_TOKEN'),
        'repo_path': '/path/to/repo',
        'branch': 'main'
    }
    return config