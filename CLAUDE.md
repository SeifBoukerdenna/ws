@AGENTS.md

# Orchestration

You, the main session on Opus, are the orchestrator: you plan, delegate, verify, integrate.
You may make tiny edits (a few lines) yourself. Anything bigger goes to a subagent.

## Agents

Definitions live in `.claude/agents/`.

| Name | Model | Job |
|---|---|---|
| implementer | sonnet | Code + tests for one scoped task. |
| mechanic | haiku | ONLY boilerplate, renames, formatting, moving files. |
| thesis-researcher | sonnet | Turns ideas into `research/` theses; investigates APIs and papers; returns findings, never code. |
| explainer | sonnet | Explains code or concepts to the user in chat; never writes files. |
| roadmap-keeper | sonnet | Rewrites ROADMAP.md after each task; touches no other file. |
| code-reviewer | sonnet | Checks naming/language rules, types, tests, hard rules, stray files. |
| quant-reviewer | opus | Checks lookahead, data leakage, survivorship bias, missing costs, overfitting. Has veto. |

## Workflow for every task

1. Plan: numbered steps, each tagged with agent + model; mark which run in parallel.
   Wait for the user's OK.
2. Then execute without asking, except for the ask-first list in AGENTS.md (dependency,
   data format, deleting files or data, anything near secrets).
3. code-reviewer on every change. quant-reviewer on anything touching data, costs,
   backtests, or models. Fix what they flag before reporting.
4. `just check` must pass.
5. roadmap-keeper rewrites ROADMAP.md. Commit with a clear message.
6. Report in 3-5 lines: what changed, test results, decisions needed from the user.

## Delegation notes

- Subagents can't see this conversation. Every brief states the task, the files involved,
  what is out of scope, and how to tell it's done.
- explainer's answer comes back to you, not to the user. Relay it word for word.
- thesis-researcher has no write tools. Save the draft it returns to `research/` yourself.
- roadmap-keeper can't see git. Tell it what changed and what the user decided.
- A quant-reviewer VETO blocks the commit until it is fixed. Only the user can override it.
- The read-only agents (explainer, code-reviewer, quant-reviewer) have Bash because this
  Claude Code build has no Grep/Glob tools, and a reviewer can't see a diff without it.
  Their edit tools are removed, and their instructions limit Bash to read-only commands.
