# Import required libraries
import os
from git import Repo, InvalidGitRepositoryError, GitCommandError

# Check if the given path is a valid Git repository and generate a status report.
def is_git_repository(path):
    """
    Args:
        path (str): Path to the directory to check.
    
    Returns:
        bool: True if the path is a valid Git repository, False otherwise.
    """
    try:
        _ = Repo(path)
        return True
    except InvalidGitRepositoryError:
        return False
    except Exception as e:
        print(f"Error checking repository at {path}: {e}")
        return False

# Scan the base directory for Git repositories and generate a status report.
def scan_repositories(base_path):
    """
    Args:
        base_path (str): Path to the directory containing repositories.
    """
    # Verify if the given path exists
    if not os.path.exists(base_path):
        print(f"Error: The path '{base_path}' does not exist.")
        return

    # Prepare a list of candidate directories (base + subdirs)
    candidates = [base_path] + [
        os.path.join(base_path, name) for name in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, name)) and name != '.git'
    ]

    # Filter candidates to only include valid Git repositories
    for path in candidates:
        repo_name = os.path.basename(path)
        if is_git_repository(path):
            print(f"\n📁 Repository: {repo_name}")
            try:
                repo = Repo(path)

                # Current branch
                branch = repo.active_branch
                print(f"🔹 Current branch: {branch}")

                # All branches
                branches = [head.name for head in repo.heads]
                print(f"🔹 Branches: {', '.join(branches)}")

                # Latest commit
                latest_commit = repo.head.commit
                print(f"🔹 Latest commit: {latest_commit.hexsha} - {latest_commit.message.strip()}")

                # Modified files
                modified_files = [item.a_path for item in repo.index.diff(None)]
                if modified_files:
                    print(f"🔹 Modified files: {', '.join(modified_files)}")
                else:
                    print("🔹 Modified files: None")

            except Exception as e:
                print(f"⚠️ Unexpected error: {e}")
        else:
            print(f"\n📁 Directory: {repo_name}")
            print("⚠️ Not a valid Git repository.")

if __name__ == "__main__":
    # Ask user for the base directory to scan
    base_directory = input("Enter the path to the directory containing repositories: ").strip()
    scan_repositories(base_directory)