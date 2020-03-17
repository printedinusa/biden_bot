
def getRecord(key):
    try:
        return record[links[key]]["text"]
    except:
        return record[0]["text"]

record = [
    {
        "name": "all",
        "text": "sorry but that issue you stated is not a valid issue key word.\n\n Check [here](https://github.com/m-leila/biden_bot/blob/master/issue_list.md) for a list of key_words"
    },
    {
        "name": "help",
        "text": "To get info on issues you can use the command `u/biden_bot *key_word*`. A list of issue key_words can be found [here](https://github.com/m-leila/biden_bot/blob/master/issue_list.md)"
    },
    {
        "name": "health_care",
        "text": "I wish everyone would stop bringing this one up. Big Pharma funds my campaign, so they obviously aren't that bad after all. Let's just cut Social Security and let them take care of us \n\n [joe Biden is funded by insurance CEOs](https://readsludge.com/2019/07/18/bernie-sanders-challenges-joe-biden-to-stop-taking-money-from-pharma-and-health-insurance-executives/) \n [Joe Biden wants to cut your social security](http://inthesetimes.com/article/21856/joe-biden-cut-medicare-social-security-retirement-age) \n [BONUS: Joe Biden personally fought to make cancer treatment unaffordable to patients in developing nations](https://www.statnews.com/2017/11/30/joe-biden-drug-pricing/)"
    },
    {
        "name": "social_security",
        "text": "social_security"
    },
    {
        "name": "race",
        "text": "race"
    },
    {
        "name": "immigration",
        "text": "immigration"
    },
    {
        "name": "foreign_policy",
        "text": "foreign_policy"
    },
    {
        "name": "criminal_justice",
        "text": "criminal_justice"
    },
    {
        "name": "drugs",
        "text": "drugs"
    },
    {
        "name": "lgbtqia+",
        "text": "lgbtqia"
    },
    {
        "name": "supreme_court",
        "text": "supreme_court"
    },
    {
        "name": "womens_issues",
        "text": "womens_issues"
    },
    {
        "name": "economy",
        "text": "economy"
    },
    {
        "name": "class",
        "text": "class"
    },
    {
        "name": "wealth",
        "text": "wealth"
    },
    {
        "name": "climate",
        "text": "climate"
    },
    {
        "name": "corruption",
        "text": "corruption"
    },
    {
        "name": "education",
        "text": "education"
    },
    {
        "name": "labor",
        "text": "labor"
    },
    {
        "name": "trade",
        "text": "trade"
    },
    {
        "name": "business",
        "text": "business"
    }
]

links = {
    "all": 0,
    "help": 1,
    "health_care": 2,
    "social_security": 3,
    "race": 4,
    "immigration": 5,
    "foreign_policy": 6,
    "criminal_justice": 7,
    "drugs": 8,
    "lgbtqia+": 9,
    "lgbt": 9,
    "lgbtq": 9,
    "lgbtq+": 9,
    "supreme_court": 10,
    "womens_issues": 11,
    "economy": 12,
    "class": 13,
    "wealth": 14,
    "climate": 15,
    "corruption": 16,
    "education": 17,
    "labor": 18,
    "trade": 19,
    "business": 20
}
