#Language selected for the assignment:Python
import re
import csv
#Step - 1: Cleaning the company names to remove stopwords, company suffixes, regional suffixes, and trailing numbers for comparison
#Function to clean the company names
def cleaning_stopwords(string):
    if not string:
        return ""
    #Make everything lowercase
    string = string.lower()

    #Remove text between brackets/parentheses(Used Google)
    string = re.sub(r'\[.*?\]|\(.*?\)', '', string)
    #Remove R&D from the string(Data based decision)
    string = re.sub(r'\br&d\b', '', string)

    #Remove punctuation(Used Google)
    string = ''.join(char for char in string if char.isalnum() or char.isspace())

    #remove extra whitespaces
    string = ' '.join(string.split())

    #Remove general stopwords
    stopwords = set(["a", "an", "the", "and"])
    #Remove company suffixes which are stopwords(some specific suffixes were specifically added based on data analysis)
    company_suffixes = set(["co", "inc", "pvt", "ltd", "llc", "lp", "lc", "plc", "corp", "sa","sse", "se", "nv", "ag", "gmbh", "hq", "com", "dept", "subsidiary", "incorporated", "company", "wholesale", "holdings", "worldwide", "coffee", "koninklijke", "international", "limited", "marketing", "systems", "finance", "group", "procurement", "division"])
    #Remove regional suffixes which are stopwords
    regional_suffixes = set(["apac", "emea", "west", "global", "north", "america", "uk"])
    
    word = string.split()
    cleaned_words = []
    for w in word:
        if w not in stopwords and w not in company_suffixes and w not in regional_suffixes:
            cleaned_words.append(w)
        #Remove any trailing numbers from the cleaned words(we remove the pincode)
        if cleaned_words and cleaned_words[-1].isdigit():
            cleaned_words.pop()
        
    cleaned_string = ' '.join(cleaned_words)
    return cleaned_string

#Step - 2: Comparing the cleaned company names to determine if they are the same company or not
#2a. Function to check if they are exactly the same company
def exact_match(string1, string2):
    return string1 == string2

#2b. Function to check if any company name is empty or undefined
def check_invalid(string1, string2):
    invalid_words = set(["", None, "unknown vendor", "null", "do not use", "see notes", "test account", "test"])
    if string1 in invalid_words or string2 in invalid_words:
        return True
    else:
        return False

#2c. Function to check if company names are contained within one another(Ex: verizon and verizon communications) (Exception: Delta and Delta Air Lines)
def contained_match(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    return words1.issubset(words2) or words2.issubset(words1)

#2d. Function to check if company and acronym match(Ex: american airlines and aa)
def check_acronym_match(string1, string2):
    #Check if one of the strings is an acronym of the other
    if len(string1) > 1 and len(string2) > 1:
        acronym1 = ''.join(word[0] for word in string1.split())
        acronym2 = ''.join(word[0] for word in string2.split())
        return acronym1 == string2 or acronym2 == string1
    return False

#2e. Function to check similarity between two strings using SequenceMatcher
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
#Check similarity to tackle spelling mistakes
def check_similarity(string1, string2):
    words1 = string1.split()
    words2 = string2.split()
    if len(words1) != len(words2):
        return False
    similarity_threshold = 0.6  # Adjust this threshold as needed(0.8 is accurate, 0.6 tackles an anomaly in a different case(P156)) PG&E and PGANDE
    #continental tire and continental airlines
    for word1, word2 in zip(words1, words2):
        score = similar(word1, word2)
        if score < similarity_threshold:
            return False

    return True

#2f. Function to check if the two company names are clearly different(should have more than 1 word)
def clearly_different(string1, string2):
    words1 = string1.split()
    words2 = string2.split()

    # Don't confidently reject short/acronym-like names
    if len(words1) == 1 or len(words2) == 1:
        return False

    common_words = set(words1) & set(words2)

    remaining1 = [w for w in words1 if w not in common_words]
    remaining2 = [w for w in words2 if w not in common_words]

    if not remaining1 or not remaining2:
        return False

    # Check whether any remaining words look similar
    for word1 in remaining1:
        for word2 in remaining2:
            if similar(word1, word2) >= 0.8:
                return False

    return True
#2g. Knowledge pairs and manually confirming them
known_pairs = {"rtx": "raytheon", "alphabet": "google", "volkswagen": "vw", "hp": "hewlettpackard", "cat" : "caterpillar", "cognizant": "cts", "federal express": "fedex", "3m": "minnesota mining manufacturing", "aeo": "american eagle", "comcast corporation": "xfinity"}
#Checking known pairs for the companies
def knowledge_match(string1, string2):
    if string1 in known_pairs:
        if known_pairs[string1] == string2:
            return True

    if string2 in known_pairs:
        if known_pairs[string2] == string1:
            return True

    return False
#Step - 3: Final answer to fill answers.csv
def classify_companies(string1, string2):
    #Clean the company names
    cleaned_string1 = cleaning_stopwords(string1)
    cleaned_string2 = cleaning_stopwords(string2)
    
    #Check if they are exactly the same company
    if exact_match(cleaned_string1, cleaned_string2):
        return 1, 0

    #Check if either company name is empty or undefined, we fill same_company column as 0, not_sure column as 0
    if check_invalid(cleaned_string1, cleaned_string2):
        return 0, 0

    #Check if company names are contained within one another
    if contained_match(cleaned_string1, cleaned_string2):
        return 1, 1

    #Check if company and acronym match
    if check_acronym_match(cleaned_string1, cleaned_string2):
        return 1, 0 #We return 1, 0 because even though we can't guarantee if they are the same company or not, we checked the data and they are the same
    
    #Check for similarity to tackle spelling mistakes
    if check_similarity(cleaned_string1, cleaned_string2):
        return 1, 1
    
    #check if the two company names are clearly different
    if clearly_different(cleaned_string1, cleaned_string2):
        return 0, 0
    
    if knowledge_match(cleaned_string1, cleaned_string2):
        return 1, 0
    #If none of the above conditions are met, return 0, 0. These are the pairs which are completely different and have length 1. We reviewed them manually and found them to be different companies. One exception is P038.
    return 0, 0


#Step - 4(Final):Code to read pairs.csv and write answers.csv
with open("pairs.csv", "r") as input_file:
    reader = csv.DictReader(input_file)

    with open("answers.csv", "w", newline="") as output_file:
        fieldnames = ["pair_id", "same_company", "not_sure"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            company_name_1 = row["name_a"]
            company_name_2 = row["name_b"]

            same_company, not_sure = classify_companies(company_name_1, company_name_2)
            writer.writerow({
                "pair_id": row["pair_id"],
                "same_company": same_company,
                "not_sure": not_sure
            })
'''
#Just for me, checking differences
old = {}
with open("answers.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        old[row["pair_id"]] = row

with open("answers_new.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        pair_id = row["pair_id"]

        if pair_id in old:
            if (
                row["same_company"] != old[pair_id]["same_company"]
                or row["not_sure"] != old[pair_id]["not_sure"]
            ):
                print(
                    pair_id,
                    "old:",
                    old[pair_id]["same_company"],
                    old[pair_id]["not_sure"],
                    "new:",
                    row["same_company"],
                    row["not_sure"]
                )

unsure_count = 0
unmatched_count = 0

with open("answers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["not_sure"] == "1":
            unsure_count += 1

        if row["same_company"] == "blah":
            unmatched_count += 1

print("Matched but unsure:", unsure_count)
print("Completely unmatched:", unmatched_count)
print("Total needing review:", unsure_count + unmatched_count)
'''
'''
print(cleaning_stopwords("3M Company"))
print(cleaning_stopwords("Minnesota Mining and Manufacturing PLC - North America"))

print(
    knowledge_match(
        cleaning_stopwords("3M Company"),
        cleaning_stopwords("Minnesota Mining and Manufacturing PLC - North America")
    )
)'''