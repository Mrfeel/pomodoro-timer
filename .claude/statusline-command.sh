#!/bin/bash
# Claude Code status line script
# Displays: directory | model | free context %

input=$(cat)

# --- Directory: last 1-2 segments of current dir ---
dir=$(echo "$input" | jq -r '.workspace.current_dir // empty')
if [ -n "$dir" ]; then
  parent=$(dirname "$dir" 2>/dev/null)
  base=$(basename "$dir" 2>/dev/null)
  if [ "$parent" != "." ] && [ "$parent" != "/" ] && [ "$parent" != "" ]; then
    pp=$(basename "$parent" 2>/dev/null)
    display_dir="${pp}/${base}"
  else
    display_dir="$base"
  fi
else
  display_dir="~"
fi

# --- Model: short display name ---
model=$(echo "$input" | jq -r '.model.display_name // empty')
if [ -z "$model" ] || [ "$model" = "null" ]; then
  model=$(echo "$input" | jq -r '.model.id // ""')
fi
short_model=$(echo "$model" | sed 's/^Claude //' | sed 's/^claude-//' | sed 's/^Haiku/Haiku/' | sed 's/^Sonnet/Sonnet/' | sed 's/^Opus/Opus/' | sed 's/-/ /g')
[ -z "$short_model" ] && short_model="?"

# --- Free context percentage ---
remaining=$(echo "$input" | jq -r '.context_window.remaining_percentage // empty')
if [ -n "$remaining" ] && [ "$remaining" != "null" ]; then
  pct=$(printf "%.0f" "$remaining")
  context_str="${pct}% free"
else
  context_str=""
fi

# --- Vim mode ---
vim_mode=$(echo "$input" | jq -r '.vim.mode // empty')
if [ -n "$vim_mode" ] && [ "$vim_mode" != "null" ]; then
  vim_str="VIM[$vim_mode]"
else
  vim_str=""
fi

# --- Assemble output ---
parts=""
[ -n "$display_dir" ] && parts="[] $display_dir"
[ -n "$short_model" ] && parts="$parts | @ $short_model"
[ -n "$context_str" ] && parts="$parts | # $context_str"
[ -n "$vim_str" ] && parts="$parts | $vim_str"

echo "$parts"
