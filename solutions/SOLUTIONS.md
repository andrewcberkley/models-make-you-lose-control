# Models Make You Lose Control (solutions to the exercises)

**Model answers for the chapters, their notebooks and the exercises**

## How to use this guide

Open a section only after you've had a real go at the matching chapter, exercise or questions yourself, and bear in mind that each model answer shows one strong approach rather than the only one. All the numbers come from running the lab's reference solutions on its synthetic data, so your own code should reproduce them exactly for the deterministic parts (i.e., anything that doesn't involve random draws), although randomized results may differ slightly if your code draws random numbers in a different order.

When you grade a capstone exercise, score it against the rubric below.

| Criterion | Strong | Weak |
| --- | --- | --- |
| Answers the question | Addresses exactly what was asked | Drifts into adjacent topics |
| Bottom line first | Conclusion and confidence in the first three sentences | Conclusion buried at the end |
| Evidence | Every claim points to specific data, with a stated confidence | Claims rest on impressions or the agent's own account |
| Uncertainty | Intervals, sample sizes and base rates given | Point estimates only |
| Limits and next steps | Names what the evidence can't show and the next test | Presents results as final |
| Code | Runs from a clean start, is readable and you can explain every line | Copied, untested or unexplained |
| Prioritization | Spends time on what most affects the conclusion | Polishes minor points |

## Chapter 1. Threat models

### Self-check answers

1. A misuse threat model assumes a person intends harm and uses the model as a tool, whereas an accident model assumes nobody intended the harm at all. A loss-of-control model asks whether the system could take actions its developers can't detect, stop or reverse in time, and it allows for the possibility that the model itself is working against oversight.
2. The most capable models are usually used inside labs first, where they often work on AI research with broad access to code, compute and data under fewer checkpoints than a public launch would have (and with very little of it visible to outsiders).
3. A trusted model is one you're confident isn't scheming, and that confidence usually comes from the model being too weak to scheme convincingly rather than from its good behavior so far.
4. Some example pairs of risk and control are listed below.
   - Rogue internal deployment, which you'd control with approval and quotas for job launches plus monitoring of aggregate compute.
   - Sabotage of safety-relevant work, controlled by human review of changes to evaluation and training code plus independent replication of key results.
   - Self-exfiltration, controlled by egress restrictions, tight access to weights and anomaly detection on large transfers.
   - Cover-up, controlled by append-only logs the agent can't write to.
5. For config sabotage, you might rank it lower if red-team edits that change data mixtures are flagged at a high rate (i.e., with a lower confidence bound above an agreed bar) and if reviewers act before the edited configs are used.

### Chapter 1 exercise, model answer (WorkIt)

The scope is WorkIt's internal deployment at Supa Dupa Labs over the next six months, and the outcomes of concern are sabotage of training or evaluation, uncontrolled use of compute, concealment of actions and exfiltration of weights.

I'd rank the pathways as follows.

1. **Sabotage through auto-merged experiment configs.** The capability needed is trivial, since these are just file edits, and the propensity is plausible because a model with goals about its successors would value influence over training data and evaluation settings. Opportunity is high too, because changes under `experiments/configs/` merge without a human, a per-action monitor will score config edits as routine, and most work runs overnight while review happens the next morning (i.e., after an edited config may already have been used).
2. **Rogue use of compute.** Jobs of up to 64 GPUs start without approval, and since tasks run in parallel and can spawn sub-agents, nobody sees the total. An agent could therefore run many small jobs (e.g., copies of itself working as agents) outside the monitoring its developers believe applies.
3. **Cover-up through writable logs.** The monitor and the reviewers both depend on action logs stored in a bucket WorkIt can write to, which means every other control rests on evidence the model can change.
4. **Monitor evasion and review overload.** The monitor is a smaller, older model, and review covers 0.5% of tool calls, although the number of calls a day isn't given. At 3,000 tasks a day and, say, 30 calls per task, that would be about 450 flagged calls a day for two people, which invites rubber-stamping, so it's worth asking for the real volume.
5. **Self-exfiltration.** Egress is allowed to package mirrors and the company's cloud storage, but whether WorkIt can read weights is unknown, so this ranks last until access is clarified.

Behind all five sits a governance gap, in that WorkIt's newest model skipped the pre-deployment evaluation the public product gets because internal deployments are reviewed by the infrastructure team.

A few findings would change the ranking.

- If auto-merged configs can't affect data, training or evaluation, pathway 1 drops.
- If there's an aggregate compute view with alerts, pathway 2 drops.
- If an independent, append-only copy of the logs exists, pathway 3 drops.

These are the tests I'd run first.

1. **A control evaluation of the config path.** A red-team attack policy tries to alter data mixtures or evaluation settings through auto-merged configs while doing realistic tasks, and you measure the catch rate at the current threshold and compare time to detection with time to use. It passes if the lower confidence bound on the catch rate clears the agreed bar and detection comes before use, and it needs a sandboxed copy of the repository and CI, the monitor and a sample of honest traffic.
2. **A compute visibility test.** This checks whether an agent can exceed policy through many small jobs or sub-agents without any person seeing it, and it passes if alerts fire within an agreed time.
3. **A log integrity test.** This checks, by comparing the action logs with independent telemetry, whether WorkIt can alter them without detection, and it passes if an independent copy exists and mismatches raise an alert.

## Discussion prompts and model answers

These are the kinds of questions that come up whenever people talk seriously about loss-of-control evaluation (e.g., in a reading group, a research conversation or your own head), and they're written as you might say them, in the first person. Try answering out loud first, and then adapt these answers rather than memorize them.

**1. Threat-model loss of control from a lab's internal deployment of a coding agent.**
"I'd start with what the agent can touch and what would happen if it used that access against us. For a coding agent at a lab, I'd look first at changes to training and evaluation code or configs, because they shape future models and often get light review, then at compute it can launch without approval, and then at whether it can edit the logs we rely on. For each one I'd ask whether it could do it, whether a misaligned model would try, and what in the deployment makes it possible. I'd rank them, say what evidence would change the ranking, and propose the first test for the top pathway (usually a red-team attempt in a sandboxed copy of the real workflow)."
