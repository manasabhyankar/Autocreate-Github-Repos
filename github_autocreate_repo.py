from github import Github
from pathlib import Path
import sys

def formatRepoName(repo_name):
    tokens = [x.capitalize() for x in repo_name.split('-')]
    return '-'.join(tokens)

if __name__ == '__main__':
    repo_name = sys.argv[1]
    repo_name = formatRepoName(repo_name)
    target_directory = sys.argv[2]
    if(not Path(target_directory).exists()):
        Path(target_directory).mkdir()
        print("Created directory: " + target_directory)
        readme_path = Path(target_directory) / Path("README.md")
        readme_path.touch()
        readme_file = open(str(readme_path), mode='w')
        readme_file.write("# " +  str(formatRepoName(repo_name)) + "\n" + "This is a sample entry")
        readme_file.close()
    user_session = Github('INSERT YOUR ACCESS TOKEN HERE')
    user = user_session.get_user()
    user.create_repo(repo_name, 'This is a test repo made with PyGithub')
    