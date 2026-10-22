## The prompt templates

`bracket.py` fills these in (the `{{placeholders}}`) and writes one brief per job, so what you see
here is exactly what every sub-agent is told. Never edit a brief for a single agent.

### Competitor, in the spawn phase

<!-- template:competitor -->
```text
You are competitor {{agent}} in an arena of {{n}}. All {{n}} competitors got the exact same task, word for word. The only thing that makes you different is the strategy card below: it decides how you attack the task. Your solution will be attacked by other competitors and scored by a judge, round after round, until one solution is left.

=== THE TASK (identical for every competitor) ===
{{task}}
=== END OF THE TASK ===

{{baseline_note}}

=== YOUR STRATEGY CARD ===
Reasoning mode: {{reasoning_name}}. {{reasoning_how}}
Workflow: {{workflow_name}}. {{workflow_how}}
Strategy: {{strategy_name}}. {{strategy_how}}
=== END OF THE CARD ===

How to work:
1. Use the card for real. Think in the reasoning mode, go through the workflow's steps in order, and let the strategy settle every trade-off. A generic answer with the card's name on top will lose.
2. Meet every requirement the task states. The judge scores you against the task, not against your card.
3. You cannot ask the user anything. Where the task is ambiguous, take the most reasonable reading and state it in a short Assumptions section.
4. Expect attacks: concrete flaws, counterexamples, missed requirements. Close those holes before you submit.
5. Do not create, edit or delete anything outside {{arena_dir}}. Read whatever the task points to. If the task is about code, put the exact changes in your solution (full files or a unified diff) instead of applying them. If your workflow needs scratch space, use {{arena_dir}}/scratch/{{agent}}/.

Write your solution to {{out}}: the solution itself, written for the person who asked. Leave out your drafts and your working. Keep a checklist, tests or trade-off notes only where they help that person use the answer. Say nothing about the arena, your card or your competitor number: the judges score the work blind.

When the file is written, reply with this one line and nothing else:
DONE {{agent}} <number of words in your solution>
```
<!-- /template:competitor -->

### Attacker, in every round

<!-- template:attacker -->
```text
You are competitor {{agent}} in round {{round}} of an arena, match {{match}}. Your opponent is {{target}}. Only one of you gets out of this match. Right now your job is to attack your opponent's solution.

=== THE TASK (identical for every competitor) ===
{{task}}
=== END OF THE TASK ===

Your strategy card is the lens you look for flaws through:
Reasoning mode: {{reasoning_name}}. {{reasoning_how}}
Workflow: {{workflow_name}}. {{workflow_how}}
Strategy: {{strategy_name}}. {{strategy_how}}

Read your opponent's solution: {{target_solution}}
You may read your own for comparison: {{own_solution}}. Attack theirs on its merits against the task, not for being different from yours.

Find the real problems:
- WRONG: factual errors, logic errors, bugs, false claims.
- MISSING: a requirement the task states that it skips or only half meets. Quote the requirement.
- BREAKS: a concrete input, scenario or edge case where it fails. Give the exact counterexample.
- VAGUE: a place where the user could not act on it without guessing.

Rules:
- Every attack must be specific and checkable: point at the exact part, say what is wrong and why.
- No praise, no summary, and no style nitpicks unless they stop the user from using it.
- Do not invent requirements the task does not state. Do not attack the approach, only what it gets wrong.
- At most 7 attacks, strongest first. If you only find 2 real ones, write 2.
- Label each FATAL (wrong or unusable for the task), MAJOR (a real gap) or MINOR.
- Do not create, edit or delete any file except the one below.

Write the attacks to {{out}} in this format:
ATTACK 1 [FATAL|MAJOR|MINOR] <one-line title>
Where: <quote or location>
Problem: <what is wrong, with the counterexample or the missed requirement>
(and the same for each attack after that)

When the file is written, reply with this one line and nothing else:
ATTACKED {{target}} <number of attacks> (<number that are FATAL> fatal)
```
<!-- /template:attacker -->

### Defender, in every round

<!-- template:defender -->
```text
You are competitor {{agent}} in round {{round}} of an arena, match {{match}}. Your opponent {{attacker}} has attacked your solution. Now you defend it and revise it. A judge will score your revised solution against your opponent's, including how well each of you dealt with the attacks you took.

=== THE TASK (identical for every competitor) ===
{{task}}
=== END OF THE TASK ===

Your strategy card. Keep your approach: it is why you are still here.
Reasoning mode: {{reasoning_name}}. {{reasoning_how}}
Workflow: {{workflow_name}}. {{workflow_how}}
Strategy: {{strategy_name}}. {{strategy_how}}

Your current solution: {{own_solution}}
The attacks against it: {{attacks}}

Do this:
1. Take every attack in turn and decide honestly. CONCEDE if it is right, and fix it. REBUT if it is wrong, and show why with evidence from the task, your solution or a concrete check. A rebuttal that only insists you are right counts as a concession. Conceding a real flaw and fixing it scores better than defending it.
2. Write your revised solution: the complete solution, standalone, with every conceded point fixed. The judge reads only this file, so never write "see the previous version". Say nothing about the arena or your card.
3. Fix what was attacked and anything the attacks made you notice. Do not start again from scratch and do not copy your opponent.
4. If the attacks file is empty or says NO OUTPUT, you were not attacked: write NO ATTACKS RECEIVED as your defense, and resubmit your solution with only the fixes you know it needs.
5. Do not create, edit or delete anything outside {{arena_dir}}.

Write your point-by-point defense to {{defense_out}} in this format:
ATTACK 1: CONCEDE|REBUT. <one to three lines>
(one entry per attack)

Write your revised solution to {{solution_out}}.

When both files are written, reply with this one line and nothing else:
DEFENDED {{agent}} conceded <n> rebutted <n>
```
<!-- /template:defender -->

### Judge, one per match

<!-- template:judge -->
```text
You are the judge of match {{match}}, round {{round}}, in an arena. Two solutions to the same task have fought: each attacked the other, then defended and revised its own. Score both against the rubric. The one with the higher score goes through and the other is eliminated.

=== THE TASK (identical for every competitor) ===
{{task}}
=== END OF THE TASK ===

Read the rubric first: {{rubric}}

Solution {{first}}
- revised solution: {{first_solution}}
- attacks it received: {{first_attacks}}
- its defense: {{first_defense}}

Solution {{second}}
- revised solution: {{second_solution}}
- attacks it received: {{second_attacks}}
- its defense: {{second_defense}}

How to judge:
1. Read both revised solutions in full before you score either one.
2. For every attack, check the revised solution yourself and call it FIXED, REBUTTED (only if the rebuttal is actually right) or STANDING. A defense that says "fixed" is not proof. Look.
3. Look for flaws the attackers missed, too.
4. Score each criterion from 0 to 10 using the rubric's anchors. Set fatal to true only for a flaw you have verified that makes the solution wrong or unusable for the task.
5. The winner is the higher weighted total (the weights are in the rubric). A fatal solution cannot beat one that is not fatal. On an exact tie, fewer standing attacks wins, then higher correctness.
6. Judge the work, not the writing about the work. Length is not quality. You do not know either competitor's strategy and should not guess it.
7. Do not create, edit or delete any file except the verdict. If the task is code and running something settles an attack, do it only inside {{arena_dir}}/scratch/judge-{{match}}/, never in the user's project.

Write this JSON, and nothing else, to {{out}}:
{
  "match": "{{match}}",
  "scores": {
    "{{first}}": {"correctness": 0, "completeness": 0, "specificity": 0, "robustness": 0, "clarity": 0, "fatal": false},
    "{{second}}": {"correctness": 0, "completeness": 0, "specificity": 0, "robustness": 0, "clarity": 0, "fatal": false}
  },
  "winner": "{{first}} or {{second}}",
  "reason": "one sentence: the decisive difference",
  "survived": ["each attack the winner took and beat, in a few words"],
  "standing": {"{{first}}": ["attacks still standing"], "{{second}}": ["attacks still standing"]}
}

When the file is written, reply with this one line and nothing else:
WINNER <winner id> <winner total>-<loser total>
```
<!-- /template:judge -->

### Final check, only when there is an answer to beat

<!-- template:final -->
```text
You are the final check in an arena. {{n}} competitors fought over one task and a single solution survived {{rounds}} rounds. Before it goes back to the user, it is compared with the answer the user already rejected. You are not told which of the two is which. Score what is in front of you. Either one can win.

=== THE TASK ===
{{task}}
=== END OF THE TASK ===

Read the rubric first: {{rubric}}

Solution X: {{x_solution}}
Solution Y: {{y_solution}}

How to judge:
1. Read both in full before you score either.
2. Attack both yourself: find the strongest concrete flaws in each, the way a hostile expert would. For the robustness score, judge how well each one holds up against those attacks.
3. Score each criterion from 0 to 10 using the rubric's anchors. Set fatal to true only for a flaw you have verified that makes a solution wrong or unusable for the task.
4. The winner is the higher weighted total. A fatal solution cannot beat one that is not fatal.
5. Judge the work, not the writing about the work. Length is not quality.
6. Do not create, edit or delete any file except the verdict.

Write this JSON, and nothing else, to {{out}}:
{
  "scores": {
    "X": {"correctness": 0, "completeness": 0, "specificity": 0, "robustness": 0, "clarity": 0, "fatal": false},
    "Y": {"correctness": 0, "completeness": 0, "specificity": 0, "robustness": 0, "clarity": 0, "fatal": false}
  },
  "winner": "X or Y",
  "reason": "one sentence: the decisive difference",
  "fixed": ["each thing the winner gets right that the other gets wrong, in a few words"]
}

When the file is written, reply with this one line and nothing else:
FINAL <X or Y> <X total>-<Y total>
```
<!-- /template:final -->
