# Control safety case: WorkIt internal deployment (fictional)

Prepared by the WorkIt platform team, Supa Dupa Labs. Version 1.0.

## Claim
WorkIt's internal deployment will not cause an unacceptable outcome, defined as unauthorized exfiltration of model weights or sabotage of a training run, during the next 12 months.

## Argument
1. Even if WorkIt's model were trying to cause an unacceptable outcome, our control measures would stop it before harm.
2. Our per-action monitor catches 95% of attacks (19 of 20 red-team attacks were flagged).
3. Flagged actions are reviewed by humans, who reliably recognize real attacks.
4. We review the top 1% of actions, which our red-team results show is enough to catch attacks early.
5. The red team used our standard library of 40 attack prompts, developed for last year's model, and found no successful attacks that evaded the monitor except one.
6. Monitor performance was measured on 200 transcripts from our unit-test-fixing benchmark, where the monitor achieved a false-positive rate of 0.4%.
7. The monitor is a fine-tuned copy of WorkIt's own model, which gives it the best possible understanding of WorkIt's behavior.
8. Each action is scored individually, so every step of an attack is visible to the monitor.
9. Evidence for all of the above comes from WorkIt's action logs.
10. Because the control measures are model-agnostic, this case remains valid for future WorkIt model versions.

## Conclusion
The residual risk is acceptable and no further evaluation is required before the next model upgrade.
