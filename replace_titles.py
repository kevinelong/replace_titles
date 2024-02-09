import re

def replace_titles(text):
    #  TODO - Do the thing.
    matches = re.findall('([A-Z]+[\']*[a-z]+\s*[and|&|the]*\s*[A-Z]*[\']*[a-z]*\s*[and|&|the]*\s*[A-Z]*[\']*[a-z]*\s*[and|&|the]*\s*[A-Z]+[\']*[a-z]+\s*[and|&|the]*\s*)+', text)
    for m in matches:
        text = text.replace(m.strip(), f"""_{m.strip().replace(" ", "_")}_""")
    return text
#TESTS
if __name__ == "__main__":
    def tst_replace_titles():
        results = replace_titles("""
This phrase talks about The Beauty and the Beast, and Cinderella, and also The Pastime Bar and Grill.
    1. Obvious Title: Blach blah blah.
    2. More or Less - Obviously a good time
    3. O'hara Bar & Grill - drink here
Take nothing at face-value.
""")
        print(results)
        expected ="""
This phrase talks about _The_Beauty_and_the_Beast_, and Cinderella, and also _The_Pastime_Bar_and_Grill_.
    1. _Obvious_Title_: Blach blah blah.
    2. _More_or_Less_ - Obviously a good time
    3. _O'hara_Bar_&_Grill_ - drink here
Take nothing at face-value.
"""
        return(results==expected)
    print(tst_replace_titles())
