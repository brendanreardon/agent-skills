#!/usr/bin/env bash
# Copy each skill in this repository (any folder containing a SKILL.md) into ~/.claude/skills.
# Usage: ./install.sh [destination]
set -euo pipefail

source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
destination="${1:-$HOME/.claude/skills}"

mkdir -p "$destination"

for skill_file in "$source_dir"/*/SKILL.md; do
    skill_dir="$(dirname "$skill_file")"
    skill_name="$(basename "$skill_dir")"
    # Other skills already in the destination are left alone.
    mkdir -p "$destination/$skill_name"
    cp -R "$skill_dir/." "$destination/$skill_name/"
    echo "Copied $skill_name -> $destination/$skill_name"
done
