JSON files contain a subset of the voter data from the PDF.

Results are split into several files:

'summary-president.json': county-wide result for presidential race.
'summary-senate.json': county-wide result for senate race.
'precincts-president.json': results for presidential race for each precinct.

TODO:
'precincts-senate.json': county-wide result for senate race.
'precincts-house.json': county-wide result for house (district 1) race.
'precincts-state-senate.json': county-wide result for state senate (district 7) race.
'precincts-state-rep.json': county-wide result for state house (district 7) race.

Each vote tally is divided by candidate and has the following keys:

'dem': democratic ticket.
'rep': republican ticket.
'lbt': libertarian ticket, if available.
'other': write-ins.
'registered': total number of registered voters (NOT votes).
'precint': name of precinct, if this tally applies to 1 precinct.

Each candidate's votes are segregated by vote type, and listed as a sequence of 3 numbers:

[election, early, provisional]

'election': on election day.
'early': early voting.
'provisional': provisional ballots.

There is also an 'all_votes' field which is the element-wise sum of all candidates' votes, including overvotes and undervotes, e.g. [election, early, provisional] across all candidates. Because of the inclusion of overvotes and undervotes in all_votes, these will not match exactly the sum across all candidates in the JSON.

