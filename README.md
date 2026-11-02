Agent skills for my personal use.

These skills (try) to follow the [Agent Skills specification](https://agentskills.io/specification) so that they can be used by any skill-compatible agent, including Claude Code or Codex.

## Skills

| Skill | Description |
| ----- | ----------- |
| [color-palette-dfci](./color-palette-dfci/) | Dana-Farber brand colors (primary, secondary, tertiary) as a hex dictionary, with rules for using them in charts. |
| [color-palette-tableau](./color-palette-tableau/) | Tableau10 and Tableau20 colors as hex dictionaries, with rules for assigning colors to categories. |
| [python-alphabetize-class-methods](./python-alphabetize-class-methods/) | Sort Python class methods into strict alphabetical (A-Z, case-sensitive) order whenever writing or editing a class. |
| [python-docstrings](./python-docstrings/) | Write or update Python function and method docstrings in Google-style format with Args, Returns, and Raises sections. |
| [python-figure-structure](./python-figure-structure/) | House style and ten-step order for matplotlib/pandas figures: Arial 6–7 pt, sizes in mm, no spines or tick marks, and export to eps, pdf, png, svg and a PowerPoint-sized png. |
| [python-import-conventions](./python-import-conventions/) | Import root modules/packages and reference members via their full dotted path, instead of importing specific names out of them. |

## Installation

Add the contents of this repository to a `~/.claude/skills/` folder (or whichever folder you're using with Claude Code).

## References

- [Claude's official Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills/tree/main) for how that repository was structured.
