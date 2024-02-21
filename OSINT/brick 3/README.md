# Brick 3

#### Author: Gourav Suram
#### Description

> After the notice that mentioned we were gonna fire him, Tom is using private repo more often. <br />
> Note: Flag is in plaintext (with different format this time)

# Writeup

- The description says `Tom is using private repo more often`
- Our goal for this challenge to find a private repo.
- There are 2 branches on the repo 

![Alt text](./imgs/image.png)

- Switch to developement repo and you'll find a pastebin link
    - under: `https://github.com/tombrickctf/company-portal/blob/development/automate/push.sh`
    - Token: `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`


- If we use git cli, it wont work. (ig git dont provide this service yet)
- We can use `Github CLI` to solve this challenge

- Reading the documentation: `https://cli.github.com/manual/gh_repo_list`
- We can use `gh repo list --visibility=private` to list out priavte repo

![Alt text](./imgs/image-1.png)

- Hmmm, error, but the intresting line is
    - `Alternatively, populate the GH_TOKEN environment variable with a GitHub API authentication token.`


- Run the following cmds:
    - `export GH_TOKEN=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`
    - `gh repo list --visibility=private`

> Note: Token validity ended.

#### Flag: 

`quarkCTF_tokens-are-moreIMP-then-privREPO`