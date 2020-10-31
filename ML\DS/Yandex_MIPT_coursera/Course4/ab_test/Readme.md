# Analysis of A/B test results.

Objectives:
- Analyze A/B test which was held on to real Yandex users.
- Confirm or deny changes in users behavior between control and experimental groups.
- Define the nature of this change and its practical significance.
- Understand which of the user groups will be the most influenced by that change.

Dataset description:

- `userID`: unique user identification number
- `browser`: browser used by the user
- `slot`: in which group the user participated in the experiment
- `n_clicks`: number of clicks that user did per `n_queries`
- `n_queries`: number of queries that user did while using `browser`
- `n_nonclk_queries`: number of queries in which user didn't click at all
