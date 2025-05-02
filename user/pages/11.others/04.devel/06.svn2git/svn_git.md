---
title: 'SVN > GIT'
metadata:
    description: 'SVN > GIT'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    limit: 5
    order:
        by: date
        dir: desc
    pagination: true
    url_taxonomy_filters: true
taxonomy:
    category:
        - corebos
    tag:
        - svn
        - git
---

- [svn2git](https://github.com/nirvdrum/svn2git)
- [Importing SVN to GitHub](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/source-code-migration-tools)
- [Converting a Subversion repository to Git](https://john.albin.net/git/convert-subversion-to-git)
- [How to migrate an SVN repository to Git](https://ao2.it/wiki/How_to_migrate_an_SVN_repository_to_Git)
- [Migrate to Git](https://www.atlassian.com/git)

### Procedure

```
mkdir svn
cd svn
svn2git https://url_to_svn_project/trunk --rootistrunk

#if that one doesn't work you can try this one:
#svn2git https://url_to_svn_project/trunk --trunk / --nobranches --notags

cd ..
git clone <git-project> import
cd import
git remote add svn ../svn
git fetch svn
git checkout -b svn svn/master
git checkout -b wip
git reset --hard $(git rev-list --max-parents=0 HEAD)
git reset $(git rev-list --max-parents=0 master)
git add -A
git commit -m <message in first commit of svn branch>
git rebase --onto wip --root svn
git tag  tagname   wip o idcommit
git checkout master
git merge svn
```

### Pull Request

```
git checkout -b temp_branch upstream/master (or upstream/branch)

git cherry-pick <SHA hash of commit>

git push origin temp_branch
```

[Send a pull request on GitHub for only latest commit](https://stackoverflow.com/questions/5256021/send-a-pull-request-on-github-for-only-latest-commit)

[Easiest way to replay commits on new git repository](https://stackoverflow.com/questions/5340790/easiest-way-to-replay-commits-on-new-git-repository)