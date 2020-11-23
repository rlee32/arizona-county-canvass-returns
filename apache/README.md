JSON files contain a subset of the voter data from the PDF.

Results are split into several files:

- 'summary-president.json': county-wide result for presidential race.
- 'summary-senate.json': county-wide result for senate race.
- 'precincts-president.json': results for presidential race for each precinct.

TODO:

- 'precincts-senate.json': results for senate race.
- 'summary-house.json', 'precincts-house.json': results for house (district 1) race.
- 'summary-state-senate.json', 'precincts-state-senate.json': results for state senate (district 7) race.
- 'summary-state-rep.json', 'precincts-state-rep.json': results for state house (district 7) race.

Each vote tally is divided by candidate and has the following keys for the candidates:

- 'dem': democratic ticket.
- 'rep': republican ticket.
- 'lbt': libertarian ticket, if available.
- 'other': write-ins.

Each candidate's votes are segregated by vote type, and listed as a sequence of 3 numbers:

[election, early, provisional]

- 'election': on election day.
- 'early': early voting.
- 'provisional': provisional ballots.

Other keys in addition to the candidates' keys are:

- 'registered': total number of registered voters (NOT votes).
- 'precinct': ID of precinct, if this tally applies to 1 precinct.
- 'all_votes': element-wise sum of all candidates' votes, including overvotes and undervotes, e.g. [election, early, provisional] across all candidates. Because of the inclusion of overvotes and undervotes in all_votes, these will not match exactly the sum across all candidates in the JSON.
