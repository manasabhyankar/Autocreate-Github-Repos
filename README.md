# Autocreate-Github-Repos
This is a simple Python automation script utilizing the Github API.

It will take the following steps to create a new repository on your Github account, as well as create the appropriate repo locally on your machine and push it to the newly created repo:
1. Run the Python script to create a new repo on your Github account.
   a. Note that this implementation uses an access token, so you will need to create one for use with your computer.
2. Create a default README.md with the name of your repo and default text.
3. Initialize a new repo at the target directory you supplied.
4. Add a default README.md file to the repo.
5. Commit with "Initial commit" as the message.
6. Set the origin to the the URL for your newly repo on your Github account.
7. Push the README.md to the origin branch (by default, this is the 'main' branch).

**Here's a template for your reference**
`new-repo <name of your repo here, excluding the angle brackets> <your target directory here>`
Example:
`new-repo Sample-Repo C:\some\sample\directory`

## Notes:
1. As mentioned before, you will need to create an access token via Github settings to use this script. Please see the instructions [here](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token) to see how to do that. You can change your access token in the **user_session** variable within the Python script.
2. This entire project is meant to be run from the command line for ease-of-access. For Windows users, this means you will need to copy **new-repo.cmd** to a directory within your PATH environment variable. This same script doesn't yet work for Linux users, but a version is planned for release...at some point. Additionally, if you don't savor the idea of adding this command to your PATH variable, you can just supply the absolute path to the script to use it (e.g C:\path\to\the\script\new-repo.cmd etc...)
3. Within the new-repo.cmd, be sure you change the URL for your Github account to that of yours (this should be on line 8 where the **origin** is set)


Keep in mind I am not responsible for any issues in your computer due to your improper copying of the **.cmd** file to a directory within your PATH variable.