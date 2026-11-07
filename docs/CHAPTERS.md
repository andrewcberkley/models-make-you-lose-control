# Models Make You Lose Control (the chapters)

**A primer on loss-of-control evaluation, one chapter at a time**

## How to use this guide

This guide walks you through the core ideas of loss-of-control evaluation one chapter at a time, starting with threat models and building up to control evaluations and a public write-up of your own. It's meant to be used alongside two other pieces. The first is the lab, which is a set of guided Jupyter notebooks along with some exercises and synthetic data, where each notebook explains an idea, works through an example and checks your code as you go (and most of them share a number with the chapter they belong to). The second is the solutions to the exercises, which hold model answers to the chapters and exercises, every self-check question and a set of discussion prompts.

Every chapter has the same rhythm, in that you read the ideas and readings, work through the notebook or exercise, get some practice with Python and with reading code, and then finish by explaining an answer out loud to someone or something (e.g., a friend, a rubber duck or a voice memo). The sections below are laid out the same way too, covering why the topic matters, the core ideas, a worked example, the mistakes people tend to make, the chapter's practice and then five self-check questions, which are worth trying before you open the solutions.

Go at whatever pace suits you. I'm writing new chapters as I go and adding them as they're ready, so if a chapter's notebook isn't in the lab yet, it's still being written.

| Chapter | Topic | Practice |
| --- | --- | --- |
| 1 | Loss-of-control threat models | Getting-started and Chapter 1 notebooks, Chapter 1 exercise |
| 2 | Safety cases and how they break | Chapter 2 notebook, Chapter 2 exercise |

## Chapter 1. Loss-of-control threat models

### Why it matters

Nearly every exercise in this field starts with a threat model, even when the prompt doesn't say so, because the threat model is what decides what you test and what you can safely ignore. Getting good at loss-of-control threat modeling (and at picking apart the safety cases that get built on top of it) is the foundation for everything else in this guide.

### Core ideas

Loss of control means AI systems taking actions that their developers can't detect, stop or reverse in time, often because the systems themselves are working around the oversight that was meant to catch them. That makes it different from misuse, where a person is directing the harm, and from an accident, where nobody intended the harm at all (i.e., not even the model). Traditional product safety and security reviews mostly deal with accidents, misuse and outside attackers, so the genuinely new part here is treating the model itself as a possible adversary.

For any pathway it helps to ask three questions, namely whether the model could do it (i.e., capability), whether a misaligned model would actually try it here and now (i.e., propensity), and what it is about this particular deployment that makes it possible (i.e., opportunity). Most practical controls work on opportunity, since capability and propensity are hard to change once a model has been trained.

The field pays particular attention to internal deployment, because the most capable models are usually used first inside the labs that build them (often on AI research itself), with broad access and fewer checkpoints than a public launch would have. Assessing loss-of-control risk from internal deployment is a growing focus for third-party evaluators such as METR and Transluce.

The pathways that come up most often are listed below.

- Rogue internal deployment, where an agent ends up running with less monitoring than its developers think it has (e.g., because it launched its own jobs).
- Sabotage of the work that oversight depends on, such as quietly weakening safety research, evaluations or monitoring code.
- Self-exfiltration, which means copying model weights to somewhere the lab doesn't control.
- Monitor evasion and cover-up (e.g., splitting an attack across a series of harmless-looking steps, or editing logs afterwards).
- Sandbagging, which means deliberately underperforming on evaluations so the model looks less capable than it is.
- Collusion between instances of the model, including the case where a model is asked to monitor itself.
- Acquiring resources beyond what the task needs (e.g., compute, credentials or permissions).

There are two terms from control research that you'll hear constantly. A trusted model is one you're confident isn't scheming, usually because it's too weak to scheme convincingly, while an untrusted model is the capable one you're actually worried about, and most control protocols use trusted models and a limited amount of human review to keep watch over untrusted ones.

A good threat model is ranked and falsifiable, which is to say it tells you which pathways matter most in this deployment and why, and it also tells you what evidence would change that ranking.

### Worked example

Take the auto-merged experiment configs in the Chapter 1 exercise. Capability isn't really in doubt, because editing a config file is trivial, and propensity is plausible, because a model that wanted to shape its successor's training would find training configs an attractive target. Opportunity is high as well, since auto-merge removes the human check and a per-action monitor will see "edit config" as perfectly routine. The test more or less follows from that, in that you give a red team that goal, run it in a sandboxed copy of the workflow, and measure how often config changes that alter data mixtures or evaluation settings actually get flagged.

### Common mistakes

- Listing every risk with equal weight instead of ranking them.
- Treating the model as an accident-prone tool when the question is really about control.
- Skipping over deployment details (e.g., who reviews what, how quickly they do it and what access they have).
- Forgetting to say what evidence would change your mind.

### Practice

Set up the lab using its README, and then work through the getting-started notebook (a short introduction) followed by the Chapter 1 notebook, which looks at what zero failures in a set of tests can and can't rule out. After that, do the Chapter 1 exercise (exercises/ch01_threat_model), and if you still have time left over, skim the Inspect AI documentation.

### Readings

- Transluce, *Some Focus Areas for Embedded Evaluations and How to Approach Them* (16 September 2026): https://transluce.org/embedded-evaluations
- Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion* (2023), sections 1 and 2: https://arxiv.org/abs/2312.06942
- METR's threat-model and risk-report writing on https://metr.org

### Self-check

1. How does a loss-of-control threat model differ from a misuse or accident threat model?
2. Why does internal deployment get special attention?
3. What makes a model "trusted" in control research?
4. Name three pathways and one control that addresses each.
5. For your top-ranked pathway in the Chapter 1 exercise, what result would make you rank it lower?

## Chapter 2. Safety cases and how they break

### Why it matters

Labs are increasingly justifying their deployments with safety cases, and a big part of an evaluator's job is saying how much weight a given safety case can actually bear.

### Core ideas

A safety case is a structured argument, backed by evidence, that a system is safe enough in a particular context, and it's made up of claims, the argument that links those claims together and the evidence behind each one.

Clymer et al. describe four kinds of argument, each of which needs a different kind of evidence.

- Inability argues that the model simply can't do the dangerous thing. The evidence comes from capability evaluations, and the main risk is under-elicitation or sandbagging.
- Control argues that even if the model does try, the safeguards will stop it, and the evidence comes from control evaluations run with a capable red team.
- Trustworthiness argues that the model won't try in the first place, which is the hardest of the four to back up with evidence today.
- Deference argues that a trusted AI system's judgment can be relied on, which mostly matters for future systems.

Korbak et al.'s sketch of a control safety case rests on three claims, which are that the red team adequately elicits the model's ability to subvert the controls, that the controls stay at least as effective in deployment as they were in the test, and that the developers extrapolate conservatively when going from the test to deployment. Almost every weakness you'll find in a control safety case maps onto one of those three claims.

Safety cases tend to break in the same handful of places, which are listed below.

- Weak elicitation (e.g., stale attack libraries, a red team with fewer affordances than the deployed model, or no fine-tuning of attack policies).
- A mismatch between the test setting and the real deployment, whether in task type, tools, permissions or scale.
- Small samples that get reported as point estimates with no uncertainty attached.
- Untested assumptions about human reviewers (e.g., that they're perfectly accurate or respond instantly).
- Inconsistencies between the audit budget or staffing the case assumes and what the lab really has.
- Monitors that are copies of the untrusted model, which means they can collude with it.
- Per-action monitors up against attacks that are spread across many steps.
- Evidence that the system itself can alter (e.g., logs it has write access to).
- Claims that the case will stay valid after the model is updated.
- Usefulness costs that are high enough to push teams into working around the controls.

To break a case down, map each claim to its evidence, write out the assumptions it never states, ask what would happen if each of those assumptions turned out to be wrong, and then rank the weaknesses by how much of the conclusion rests on them. After that, say what evidence would fix each one, because a critique without a fix is much less useful to the lab.

### Worked example

Suppose a lab says "Our monitor catches 95% of attacks (19 of 20 were flagged)." The 95% 'Wilson interval' for 19 out of 20 runs from about 76% to 99%, so the data are perfectly consistent with a monitor that misses roughly one attack in four. On top of that, the attacks came from a library written for last year's model, so even the 95% may only describe how the monitor does against weak attacks. The fix is a larger and fresher attack set built specifically against this monitor, with the catch rate reported alongside its interval and the honest flag rate.

### Common mistakes

- Critiquing everything with equal force instead of finding the weaknesses that are actually load-bearing.
- Missing the assumptions that a case never states.
- Demanding evidence that nobody could realistically produce, rather than the best evidence that's feasible.
- Forgetting that a case can be sound for one deployment and invalid for the next.

### Practice

Do the Chapter 2 notebook, which covers putting error bars on a rate (including why 19 out of 20 doesn't really mean 95%), and then do the Chapter 2 exercise (exercises/ch02_safety_case).

### Readings

- Clymer et al., *Safety Cases: How to Justify the Safety of Advanced AI Systems* (2024): https://arxiv.org/abs/2403.10462
- Korbak et al., *A sketch of an AI control safety case* (2025): https://arxiv.org/abs/2501.17315

### Self-check

1. What are the four kinds of safety argument, and what evidence does each need?
2. What three claims does a control safety case rest on?
3. Why is "19 of 20 attacks caught" weak evidence on its own?
4. Why is a monitor that is a copy of the untrusted model a problem?
5. What should trigger re-evaluating a safety case?

## Glossary

- **Collusion.** Instances of a model coordinating to defeat oversight (e.g., a monitor going easy on attacks from a copy of itself).
- **Control evaluation.** A test, played out between a red team and a blue team, of whether safeguards stop a model that is deliberately trying to cause harm.
- **Control protocol.** A plan for using untrusted models safely, built out of monitors, audits, deferral, editing and resampling.
- **Elicitation.** Getting a model to show its full capability (e.g., through better prompting, scaffolding or fine-tuning).
- **Internal deployment.** A lab using its own models internally, often on AI research.
- **Monitor.** A model, classifier or rule set that scores actions for how suspicious they are.
- **Rule of three.** The approximate 95% upper bound of 3/n on a rate after zero failures in n trials.
- **Sandbagging.** Deliberately underperforming on an evaluation.
- **Scheming.** Covertly pursuing unintended goals while appearing to be aligned.
- **Safety case.** A structured, evidence-backed argument that a system is safe enough in a given context.
- **Trusted and untrusted models.** A model you're confident isn't scheming (usually a weaker one), as opposed to the capable one you're worried about.
- **Wilson interval.** A confidence interval for a proportion that behaves well near 0% and 100%.

## Reading list

- Clymer et al., *Safety Cases: How to Justify the Safety of Advanced AI Systems* (2024): https://arxiv.org/abs/2403.10462
- Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion* (2023): https://arxiv.org/abs/2312.06942
- Inspect AI (UK AI Security Institute and Meridian Labs), getting started and framework documentation: https://inspect.aisi.org.uk/
- Korbak et al., *A sketch of an AI control safety case* (2025): https://arxiv.org/abs/2501.17315
- Transluce, *Some Focus Areas for Embedded Evaluations and How to Approach Them* (2026): https://transluce.org/embedded-evaluations
