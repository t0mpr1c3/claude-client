#!/home/tesco/claude/claude-client/claude/bin/python

# usage:
# ./claude.py user_prompt.txt

import anthropic
import os
import sys
import re

# Set your Anthropic API key as an environment variable
# export ANTHROPIC_API_KEY="YOUR_API_KEY"
api_key = os.environ.get("ANTHROPIC_API_KEY")

brk = "=" * 80 + "\n"

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable not set.")

client = anthropic.Anthropic(api_key=api_key)

def send_prompt_to_claude(prompt_text, model="claude-sonnet-4-5-20250929"):
    """
    Sends a prompt to Claude and returns the generated response.
    """
    try:
        response = client.messages.create(
            model=model,
            max_tokens=20000,  # Adjust as needed
            messages=[
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.content[0].text
    except Exception as e:
        print(f"ERROR SENDING PROMPT TO CLAUDE: {e}")
        return None

def extract_and_save_code(claude_response, default_filename="generated_code.py"):
    """
    Extracts code blocks from Claude's response and saves them to a file.
    Assumes code is within markdown code blocks (```language ... ```) with the filename in a comment above the block.
    """
    code_blocks = []
    file_names = []
    in_code_block = False
    current_code = []
    last_comment = None

    for line in claude_response.splitlines():
        if line.strip().startswith("#") and not in_code_block:
            last_comment = re.sub("^[# ]*", "", line.strip())
        elif line.strip().startswith("```") and not in_code_block:
            in_code_block = True
            current_code = [] # Reset for new code block
            filename = default_filename
            if last_comment != None:
                filename = last_comment
            file_names.append(filename)
        elif line.strip().startswith("```") and in_code_block:
            in_code_block = False
            code_blocks.append("\n".join(current_code))
        elif in_code_block:
            current_code.append(line)

    for block, filename in zip(code_blocks, file_names):
        with open(filename, "w") as f:
            f.write(block)
        print(brk + f"CODE BLOCK SAVED TO {filename}\n" + brk)
    else:
        print(brk + f"NO CODE BLOCKS FOUND IN RESPONSE.\n" + brk)

if __name__ == "__main__":
    prompt_filename = sys.argv[1];
    with open(prompt_filename, 'r') as file:
        user_prompt = file.read();
        print(brk + f"SENDING PROMPT TO CLAUDE:\n" + brk + f"{user_prompt}\n")
        claude_response = send_prompt_to_claude(user_prompt)
        if claude_response:
            print(brk + f"RESPONSE FROM CLAUDE:\n" + brk + f"{claude_response}\n")
            extract_and_save_code(claude_response, "claude.log")
        else:
            print(brk + f"I CAN'T HEAR YOU CLAUDE.\n" + brk)
