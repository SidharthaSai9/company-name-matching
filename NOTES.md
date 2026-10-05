Submitted answers.csv, NOTES.md, and company_matching.py, a python file which solves the question.

How to run the python file:

Place company_matching.py and pairs.csv in the same folder. We do not need to install any python package to run the file. The file will automatically create answers.csv containing pair_id, same_company, not_sure

Questions to be answered:

1. **What did you do about the knowledge pairs** — the ones text comparison can't solve?
   How did you find them, what did you decide, and what would you do differently with more time?
Ans. I had 6 main conditions to figure out whether the company was same or not, or atleast get some evidence supporting the statement. After that, I manually inspected the cases untouched by these 6 conditions, and defined a few specific companies as knowledge pairs. I did not find 30 though, I found 10 - 15. 

2. **How many did you get right?** We didn't give you the answers — so to know how you did,
   you'll have to work some out yourself. Tell us how you did that, and how many you checked.
Ans. I have 22 "not sures", I took the safe approach in a few cases. For example, if name A is a subset of name B, they are the same company, but not sure and should be checked manually. The 22 "not sures" are correct upto my knowledge
"P113,First Republic - APAC,First Republic Bank Corp" I am not sure about this after manual checking. My code gives they are same, but not sure.
My code gives yes but not sure for delta and delta dental(P138), but gives different and sure for P096,"Delta, Corporation, Marketing","Delta Dental Plans Association, NV (Procurement)".
My code gives P157,"WF, Lgal",Wells Fargo / Group as different and sure, but they are the same. 
My code gives P038,"Citibank, PLC, UK","Ciitigroup, L.L.C." as different and sure, but they are the same.
My code gives P176,Cosstco,Costco Wholesale Corporation 24792 as different and sure, but they are the same.


3. **Which mistake is worse:** saying two different companies are the same, or missing that
   two names are the same company? Pick one, say why, and tell us if it changed what you built.
Ans. In my opinion, saying two companies are same is worse than missing that two names are the same company. If two different companies are merged, their records could get mixed together, but if two same companies are kept separately, we can have easy access for someone to manually review it and correct it. It changed what I built when I was selecting the threshold for the fuzzy matching of similar strings. High threshold does not select companies which are different but sound similar. This can be compared to "being more safe than sorry"

4. **Show us one your program got wrong,** and explain why it got confused.
P105,"Oracle Corporation, Co.","Oracl, LLC"
P124,Chvron,CHEVRON CORPORATION
P176,Cosstco,Costco Wholesale Corporation 24792
These are three cases which turned out wrong. I could not use corporation as a company suffix stopword, because progressive corporation and progressive leasing are two different companies. My subset condition should normally work, but the spelling cases dont let it work here. Trying fuzzy matching fails because the company name does not match with corporation. So it fails. We can maybe add a condition in the fuzzy matching function to NOT check with corporation and that would work.

5. **What did you have to learn?** Something you didn't know when you started — where you
   learned it, and what confused you at first.
I did not know how to solve the spelling mistake issue. It is clear for the human eye, but I didn't get any idea to code. I learnt it in stackoverflow, an online website. I didn't know a direct function existed to check how similar two words are. This was something I had to learn. 

What I didn't get to do:
I wanted to fuzzy match with "corporation" but I didn't have time and couldn't get the idea until later in the day. \
I am not sure if delta is delta airlines, or delta dental, or completely different. I couldn't find any valid source online, and that confused me. The results related to that still confuse me.

Where I used AI and where it helped:
I used copilot to help me with coding the trivial initial functions. I write the comments and it gives the code. It was correct for most of it, the stopwords/company_suffixes was one place I remember AI being different than what I wanted to use. I used the internet to search for fuzzy matching, and how to remove text between brackets.(I could've directly used copilot here as well)

Libraries I used are:
difflib, csv, re. All of these are builtin libraries in python.
