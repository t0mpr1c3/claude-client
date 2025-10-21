# claude-client
Simple script to dispatch prompts to Claude Sonnet 4

Usage:
```bash
./claude.py user_prompt.txt
```

Dependencies:
```bash
sudo apt install python3-venv
sudo apt install python3-pip
mkdir -p claude
python3 -m venv claude
source ./claude/bin/activate
python3 -m pip install anthropic
```

Setup:
```bash
./setup.sh
source ./claude/bin/activate
```

Set your Anthropic API key as an environment variable:
```bash
export ANTHROPIC_API_KEY="YOUR_API_KEY"
```

For more information, see https://docs.claude.com/en/api/overview#python
