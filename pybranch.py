import sys
import subprocess

from git.exc import InvalidGitRepositoryError
from git import Repo
from simple_term_menu import TerminalMenu

new_branch_shortcut = "ctrl-n"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        try:
            repo = Repo(path)
        except InvalidGitRepositoryError:
            print(f"No git repository found in {path}")
            exit()
    else:
        try:
            repo = Repo()
        except InvalidGitRepositoryError:
            print("Not git repository found in this directory")
            exit()

    all_branches = [head.name for head in repo.heads]
    all_branches.remove(repo.active_branch.name)
    all_branches = [repo.active_branch.name + " (active)"] + all_branches

    terminal_menu = TerminalMenu(all_branches, title=f"Switch branch ({new_branch_shortcut} for creating a new branch)",
                                 accept_keys=(new_branch_shortcut, "enter"))

    index = terminal_menu.show()
    accept_key = terminal_menu.chosen_accept_key

    if accept_key == "enter":
        if index == 0:
            print("Remaining on same branch")
        else:
            subprocess.run(["git", "checkout", all_branches[index]])

    if accept_key == new_branch_shortcut:
        name = input("Branch name: ")
        subprocess.run(["git", "checkout", "-b", name])
