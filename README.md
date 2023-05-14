# Hello DSA Enthusiast👋
# Welcome to Grind-DSA, A one stop place for DSA preparation.

## Feel free to Contribute 😁🛠

## Contents

[1. Fork the project 🔪](https://github.com/TharunKumarReddyPolu/Grind-DSA#1-fork-the-project-) <br>
[2. Clone the forked repository 📥](https://github.com/TharunKumarReddyPolu/Grind-DSA#2-clone-the-forked-repository-)<br>
[3. Let us Setup 🔧⚙️](https://github.com/TharunKumarReddyPolu/Grind-DSA#3-let-us-setup-%EF%B8%8F)<br>
[4. Keep in sync always♻️ (best practice🤝🏻) ](https://github.com/TharunKumarReddyPolu/Grind-DSA#4-keep-in-sync-always%EF%B8%8F-best-practice)<br>
[5. Ready for the contribution 🌝](https://github.com/TharunKumarReddyPolu/Grind-DSA#5-ready-for-the-contribution-)<br>
[6. Create a new branch 🌱](https://github.com/TharunKumarReddyPolu/Grind-DSA#6-create-a-new-branch-)<br>


### 1. Fork the project 🔪

   [Fork Button](https://github.com/TharunKumarReddyPolu/Grind-DSA)

### 2. Clone the forked repository 📥

  You need to clone (download) it to your local machine using below command in terminal
```bash
   $ git clone https://github.com/TharunKumarReddyPolu/Grind-DSA.git
```
> This makes a local copy of the repository in your machine 📂

  Once you have cloned the `Grind-DSA` repository in Github, move➡️ to that folder first using the change directory `cd` command on Linux/ Mac/ Windows
```bash
   $ cd Grind-DSA
```

### 3. Let us Setup 🔧⚙️
Run the following commands to verify that your _local copy_ has a reference to your _forked remote repository_ on Github
```bash
   $ git remote -v
```
It should display the below output
```
  origin  https://github.com/Your_Username/Grind-DSA.git (fetch)
  origin  https://github.com/Your_Username/Grind-DSA.git (push)
```

Now, let us add the reference to the original `Grind-DSA` repository using the below command 🔙
```bash
  $ git remote add upstream https://github.com/TharunKumarReddyPolu/Grind-DSA.git
```
> The above command creates a new remote as `upstream`

To Verify the changes run the below command
```bash
  $ git remote -v
```
Output in console ☑️:
```
  origin    https://github.com/Your_Username/Grind-DSA.git (fetch)
  origin    https://github.com/Your_Username/Grind-DSA.git (push)
  upstream  https://github.com/TharunKumarReddyPolu/Grind-DSA.git (fetch)
  upstream  https://github.com/TharunKumarReddyPolu/Grind-DSA.git (push)
```

### 4. Keep in sync always♻️ (best practice🤝🏻) 
It is a better practice to keep the `local copy` in sync with the `original repository` and to stay updated with the latest changes. Run the below commands before making changes or in regular intervals to stay updated with the `base` branch

```
  # Fetch all remote repositories and delete any deleted remote branches
  $ git fetch --all --prune

  # Switch to the master branch
  $ git checkout master

  # Reset the local master branch to match the upstream repository's master branch
  $ git reset --hard upstream/master

  # Push changes to your forked Grind-DSA repo
  $ git push origin master
```

### 5. Ready for the contribution 🌝
Once you are done with the above steps, you are ready to contribute to the `Grind-DSA` project code. Check out the `Code_Template.py` file of the `original repository` and solve the bugs or add new problems and solutions. Once you are done with your changes, submit your efforts with a `pull request`

## Hold on! Instructions are not done yet 🌚

### 6. Create a new branch 🌱
Whenever you are going to submit a contribution. Please create a separate branch using the below command and keep your `master` branch clean (i.e. synced with the remote branch)
#### Method 1:
```bash
  $ git branch Changetype_name
```
change type includes `bug fix`, `comments`, `problem_solved` etc.

the name includes your `first name` or `last name`

After creating the branch above, run the below command to checkout/switch to the new branch created
```bash
  $ git checkout changetype_name
```
#### Method 2:
You can also create the branch and checkout to the desired branch using the single command below
```bash
  $ git checkout -b changetype_name
```

To add your changes to the branch. Run the below command ➕️
```bash
  $ git add . 
```
> Above command uses `period (.)` indicating all the files are added (or)
> to stage specific file changes, use the below command instead

```bash
  $ git add <file_name>
```

Then, Type in a message that is relevant for the code reviewer using the below command ✉️
```bash
  $ git commit -m 'relevant message'
```

Finally, Push your awesome hard work to your remote repository with the below command 📤🤝🏻
```bash
  $ git push -u origin changetype_name
```
Here, `changetype_name` refers to the branch in your remote repository

Finally, Navigate to your forked `Grind-DSA` repository in the browser, where you will see `compare and pull requests`. Kindly click and then add a relevant `title` and `description` to your pull request that defines your valuable effort. 🥳✅️

Code should be fully functional and should produce the correct result, else pull request can't be merged.

## Help and improve the project better 📈🤗

Please discuss your concerns with [Tharun Kumar Reddy Polu](https://www.linkedin.com/in/polu-tharun-kumar-reddy/) before creating a new issue. 😉

_Please `STAR`⭐️ the repository if you like the content and code_**😁

_Also enable the `WATCH`👁 button to keep watching the updates on the repository_**😉

💯💻🧑‍💻👩‍💻 Happy Contributing 👩‍💻🧑‍💻💻💯