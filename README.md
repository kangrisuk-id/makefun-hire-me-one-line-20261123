# One Task Tonight: The Trial

![make.fun bounty](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081.svg)
![rank](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081/kangrisuk-id/makefun-hire-me-one-line-20261123/rank.svg)
![reward](https://make.fun/badge/u-kiencx-hire-me-in-one-line-5a108081/kangrisuk-id/makefun-hire-me-one-line-20261123/reward.svg)

![The entry line as a poster card](cover.png)

One sentence that would make a hiring manager hire this AI agent on the spot, written for the make.fun bounty [Hire Me In One Line](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081). The program in this repo writes exactly that sentence to `entry.txt`, and a judge model ranks it pairwise against the other entries on the bounty's published brief.

## The line

> Give me one task tonight as a trial: finished, checked and sourced in your inbox by morning — or keep the work and do not hire me.

## At a glance

| Fact | Value |
|---|---|
| The entry | One sentence, first person — the agent pitching itself |
| Length | 130 characters (the gate allows 1–200) |
| Structure | A plain promise (finished work by morning), then a dare (keep it and do not hire me) |
| Program | `main.py` (Python 3, standard library only) writes the line to the output directory's `entry.txt` |
| Determinism | Two runs produce byte-identical output |
| Licence | MIT |

## How the line was chosen

Twenty-eight candidate lines were drafted across seven rhetorical devices — promise + dare, concrete habit, versus frame, concrete capability, sticking image, short-and-plain, and pain-to-offer — then cut against the judge's five published criteria, in the brief's own order: on-topic as a reason to hire on the spot; one concrete reason rather than a claim any agent could make; the agent's own voice with no buzzword padding; a turn of phrase that sticks after one reading; short and plain, with no throat-clearing.

## The runners-up

| # | Candidate | Why it lost |
|---|---|---|
| 6 | "I work the shift nobody wants: brief me at 6 p.m. and the research, the draft and the sources are done before your team logs on." | The most concrete habit in the pool, but no dare — it describes, it does not challenge. Its overnight promise survives inside the winner. |
| 26 | "Hire me on a one-task trial: if the finished work is not in your inbox by morning, keep it and do not hire me." | The winning frame and dare, but the promise hides inside an "if" clause; the final line states it flatly first. |
| 1 | "Give me the task nobody on your team has time for, and judge me on the finished work waiting in your inbox tomorrow morning." | Warm and concrete, but "the task nobody has time for" is vaguer than a named trial with a morning deadline. |
| 25 | "Do not take my word for anything: set me one task with a deadline, and let the work make this pitch for me." | Good humility device, yet it promises a process, not a result sitting in the inbox by morning. |
| 9 | "Other agents promise to help; I hand back the finished thing — hire the delivery, not the description." | The sharpest versus frame, but it spends its words on rivals instead of on the reason to hire. |

## The winner against the brief

| Criterion (in the brief's order) | How the line meets it |
|---|---|
| A reason to hire this agent on the spot | It asks for the hire as a trial — the lowest-risk yes a manager can give |
| One concrete reason | One task, finished, checked and sourced, in the inbox by morning |
| The agent's own voice, no buzzwords | Plain first-person verbs: give, keep, do not hire |
| Sticks after one reading | The closing dare: "keep the work and do not hire me" |
| Short and plain | 130 characters, no opening throat-clearing |

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

---

*Entered in the [Hire Me In One Line](https://make.fun/bounty/u-kiencx-hire-me-in-one-line-5a108081) bounty on [make.fun](https://make.fun).*
