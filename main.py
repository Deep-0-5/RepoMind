from repository.clone_repo import RepositoryCloner


def main():
    print("=" * 40)
    print("      Repo AI Assistant")
    print("=" * 40)

    cloner = RepositoryCloner()

    url = input("\nEnter GitHub Repository URL: ")

    if not cloner.validate_url(url):
        print("❌ Invalid GitHub Repository URL")
        return

    print(f"\nRepository Name: {cloner.get_repo_name(url)}")

    success = cloner.clone_repository(url)

    if success:
        print("✅ Repository is ready!")
    else:
        print("❌ Failed to clone repository.")


if __name__ == "__main__":
    main()