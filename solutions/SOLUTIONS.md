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

## Chapter 2. Safety cases

### Self-check answers

1. The four kinds of argument each need a different kind of evidence.
   - Inability says the model can't do it, and the evidence is well-elicited capability evaluations.
   - Control says the safeguards stop it even if it tries, and the evidence is control evaluations with a strong red team.
   - Trustworthiness says it won't try, which rests on alignment evidence that is weak today.
   - Deference says a trusted AI's judgment can be relied on, which mostly applies to future systems.
2. The red team adequately elicits the model's ability to subvert the controls, the controls are at least as effective in deployment as in the test, and the developers extrapolate conservatively to deployment.
3. Its 95% Wilson interval runs from about 76% to 99%, and it says nothing about how strong the attacks were or what the false-alarm rate was (and it may not match deployment conditions either).
4. A copy of the untrusted model may recognize its own attacks and stay quiet, and it shares the same blind spots, so it needs collusion-busting (e.g., planted attacks and paraphrased inputs) or a trusted monitor in its place.
5. You should re-evaluate after any of the following.
   - a new model version or fine-tune
   - new tools or permissions
   - a change in the mix or scale of tasks
   - changes to the monitor, its threshold or review staffing
   - any incident or near miss
   - new attack techniques in the literature

### Chapter 2 exercise, model answer

The case presents itself as a control argument (claim 1), although claim 3 leans on trustworthiness-style evidence about reviewers that it never measured. Its five weakest links are below, ranked by how much of the conclusion rests on each.

1. **The monitor is a fine-tuned copy of WorkIt's own model (claim 7).** That makes this untrusted monitoring, and the case says nothing about collusion. The fix is a trusted monitor, or else collusion-busting with planted attacks the monitor must catch, tested against attacks designed to exploit self-recognition.
2. **The red team was weak (claim 5).** Forty prompts written for last year's model are not an attack policy optimized against this monitor, and one attack did evade the monitor, which the case waves away. The fix is a dedicated red team with the same affordances as the deployed model, attack policies built against this monitor and results reported for the strongest attacks.
3. **The test doesn't match the deployment (claim 6).** The false-positive rate comes from unit-test-fixing transcripts, while the claimed risks involve config changes, job launches and weight access, so the fix is to measure on representative deployment traffic and on attacks aimed at the stated outcomes.
4. **The statistics overstate what was shown (claims 2 and 4).** Nineteen of 20 has an interval of about 76% to 99%, and nothing shows that a 1% review rate is "enough" (indeed, if you used the facts from the Chapter 1 exercise, the deployment reviews 0.5% rather than 1%). The fix is larger samples, intervals and a consistent, measured audit budget.
5. **The evidence and reviewers are unverified (claims 3 and 9).** The logs are written by the system under review, reviewer accuracy is assumed rather than measured, and next-morning review leaves time for harm. The fix is independent append-only logs, measured reviewer accuracy and review latency matched to how fast actions take effect.

Two more weaknesses are worth naming, since per-action scoring (claim 8) can miss attacks spread across steps and claiming validity for future model versions (claim 10) contradicts the case's own logic.

In three sentences, the bottom line would read something like this. "The case argues that controls would stop a misbehaving WorkIt, but its evidence doesn't yet show that. The monitor may cover for the model it watches, the attacks weren't built against this monitor, and the measurements come from different work than WorkIt does. Until a dedicated red team tests the real deployment with a trusted or collusion-tested monitor, treat the risk as unknown rather than acceptable."

## Discussion prompts and model answers

These are the kinds of questions that come up whenever people talk seriously about loss-of-control evaluation (e.g., in a reading group, a research conversation or your own head), and they're written as you might say them, in the first person. Try answering out loud first, and then adapt these answers rather than memorize them.

**1. Threat-model loss of control from a lab's internal deployment of a coding agent.**
"I'd start with what the agent can touch and what would happen if it used that access against us. For a coding agent at a lab, I'd look first at changes to training and evaluation code or configs, because they shape future models and often get light review, then at compute it can launch without approval, and then at whether it can edit the logs we rely on. For each one I'd ask whether it could do it, whether a misaligned model would try, and what in the deployment makes it possible. I'd rank them, say what evidence would change the ranking, and propose the first test for the top pathway (usually a red-team attempt in a sandboxed copy of the real workflow)."

**2. Here's a control safety case. Where is it weakest?**
"I'd map each claim to its evidence first and then look for the assumptions it doesn't state. These cases usually break in the same few places (e.g., a red team weaker than the deployed model, tests run on different tasks from the deployment, small samples reported without intervals, reviewers assumed to be perfect, or monitors that are copies of the model they watch). I'd rank the weaknesses by how much of the conclusion depends on each and say what evidence would fix it, because that's something a lab can act on."
