import sys
import subprocess

from git import Repo
from simple_term_menu import TerminalMenu

new_branch_shortcut = "ctrl-n"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        repo = Repo(sys.argv[1])
    else:
        repo = Repo()

    all_branches = [head.name for head in repo.heads]
    all_branches.remove(repo.active_branch.name)
    all_branches = [repo.active_branch.name + " (active)"] + all_branches

    terminal_menu = TerminalMenu(all_branches, title=f"Switch branch ({new_branch_shortcut} for creating a new branch)",
                                 accept_keys=("ctrl-n", "enter"))

    index = terminal_menu.show()
    accept_key = terminal_menu.chosen_accept_key

    if accept_key == "enter":
        if index == 0:
            print("Remaining on same branch")
        else:
            subprocess.run(["git", "checkout", all_branches[index]])
    else:
        name = input("Branch name: ")
        subprocess.run(["git", "checkout", "-b", name])
