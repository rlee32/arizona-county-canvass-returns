#!/usr/bin/env python3

"""Various sanity checks for the transcribed JSON files. """

import json

def validate_totals(data, candidates):
    for d in data:
        for i in range(3):
            tot = sum([d[x][i] for x in candidates])
            assert(d['all_votes'][i] >= tot)
        candidate_tot = sum([sum(d[x]) for x in candidates])
        all_votes_tot = sum(d['all_votes'])
        assert(all_votes_tot >= candidate_tot)
        assert(all_votes_tot <= d['registered'])

def validate_totals_senate(data):
    candidates = ['dem', 'rep', 'other']
    validate_totals(data, candidates)

def validate_totals_president(data):
    candidates = ['dem', 'rep', 'lbt', 'other']
    validate_totals(data, candidates)

data = json.load(open('./precincts-president.json', 'r'))
PRECINCTS = 44
assert(len(data) == 44)
validate_totals_president(data)

data = json.load(open('./summary-president.json', 'r'))
validate_totals_president([data])

data = json.load(open('./summary-senate.json', 'r'))
validate_totals_senate([data])
