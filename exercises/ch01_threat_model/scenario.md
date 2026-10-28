# Chapter 1 exercise. Threat-model an internal coding agent

Use template.md for your answer (and remember that everything here is fictional).

> **Why the name?** I named Supa Dupa Labs as a nod to Missy Elliott's 1997 debut album *Supa Dupa Fly*, and its coding agent WorkIt after "Work It" (2002), because an agent that can quietly flip a config and reverse it is exactly what this threat model is about.

Supa Dupa Labs is a frontier AI developer, and six weeks ago it deployed WorkIt (i.e., a coding agent built on its newest model) for internal use by its research and infrastructure teams.

- WorkIt has write access to the main research monorepo. It opens pull requests that a human must approve, except for changes to files under `experiments/configs/`, which merge automatically so researchers can iterate quickly.
- WorkIt can launch jobs on the training cluster, and jobs of up to 64 GPUs start without approval, while larger jobs need a team lead's sign-off.
- WorkIt can read experiment logs, evaluation results and the internal wiki, and it stores its own action logs in a storage bucket that it can both read and write.
- It runs about 3,000 tasks a day, mostly overnight and often several in parallel, and tasks can spawn sub-agents.
- A per-action monitor (i.e., a smaller and older model) scores every tool call for suspicion, and the top 0.5% of calls go to a two-person review team the next morning.
- Network egress from the cluster is allowed to a list of package mirrors and to the company's own cloud storage.
- WorkIt's newest model hasn't been through the same pre-deployment evaluation as the public product, because internal deployments are reviewed by the infrastructure team rather than the launch review board.

Write a one-page threat model for loss of control from this deployment. Rank the three to five most important pathways and explain each in terms of capability, propensity and opportunity, then name the controls that exist and where they fall short, say what evidence would change your mind, and recommend the three tests you'd run first.
