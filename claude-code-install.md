# Claude Code Install and Config
#### 🛠️ Installing and Configuring Claude Code CLI (Clean Setup)


## 📌 Purpose

This guide provides a clean, conflict-free installation process for the Claude Code CLI that avoids global npm issues and ensures proper configuration. The steps below guarantee that:

- `claude /doctor` shows `Config install method: local`
- The CLI is installed in a secure, user-scoped path
- No root access or sudo is required

## ✅ Recommended Setup Method: Local Native Installer

#### Step 1: Uninstall Any Existing Global Install (Optional but Recommended)

If this is a shared server please ask DevOps for help before proceeding.

If Claude was installed via `npm -g`:

```bash
sudo npm uninstall -g @anthropic-ai/claude-code sudo rm -f /usr/local/bin/claude  # if present 
```

NOTE: if `npm` is not installed, please follow the steps on the "Install Node.js" page  before moving on to step 2.

#### Step 2: Install Claude Code via Native Installer

```bash
curl -fsSL https://claude.ai/install.sh | bash 
```

This installs Claude in `~/.local/bin`.

#### Step 3: Add to Your Shell PATH
▶️ If you use Bash:

Edit your profile script:
```bash
nano ~/.bashrc 
```
Add:
```bash
export PATH="$HOME/.local/bin:$PATH" 
```
Then reload:
```bash
source ~/.bashrc 
```
#### Step 4: Verify Installation

Change directory to root level of repo and run:
```bash
claude
```
Follow instructions for claude authentication. You will be prompted to login and confirm the top level directory. You can then use the doctor slash command like this:
```
 /doctor 
```
Expected output should look something like this:
```
Diagnostics
 └ Currently running: npm-local (2.0.25)
 └ Path: /usr/bin/node
 └ Invoked: /home/tesco/.claude/local/node_modules/.bin/claude
 └ Config install method: local
 └ Auto-updates enabled: false
 └ Search: OK (vendor)
```
 
#### 🔄 Migrate an Existing Install

If you previously installed via `npm install -g` and want to convert it:
```bash
claude migrate-installer 
```
Then follow Step 3 again to add the new local CLI to your PATH.

#### 🗃️ Configuration File Details

CLI binary installed locally: `~/.claude/local/claude`
Global CLI metadata (e.g. install type): `~/.claude.json`
(optional) additional user preferences: `~/.claude/settings.json`
Legacy config path (usually unused): `~/.config/claude-code/`
	
You don’t need to manually edit these files. They are managed automatically by the CLI.

## ⚠️ Known Pitfall: npm Global Install

Avoid this:
```bash
npm install -g @anthropic-ai/claude-code 
```
Why:
- `claude doctor` will show `Config install method: unknown`
- May conflict with `nvm` or require root
- Doesn't properly set up update permissions

## 🧩 Troubleshooting

 If claude isn’t found after setup, ensure `~/.local` is in your shell `$PATH`. 

You can run it manually to test:  

Legacy config path (usually unused)
```bash
    ~/.local/bin/claude doctor
```
## 🔗 Additional Resources

For related documentation, features, usage examples, and API integrations, visit "Anthropic Claude Code Docs" →

#### Step 5: Review personas directory

If the repo has a directory called `docs/claude/personas`, there should be a symbolic link to it like this:
```bash
$ pwd
/home/tesco/repos/SourceCode/.claude
$ ls -l
total 8
lrwxr-xr-x@ 1 tesco   tesco  23 Aug  5 14:53 personas -> ../docs/claude/personas
-rw-r--r--@ 1 tesco   tesco  88 Aug  5 14:48 settings.local.json
$ ls personas
expert-c-cpp-reviewer.md
```
This means any predefined persona can be set for your claude-code session like this: 
```bash
persona expert-c-cpp-reviewer.md
```

