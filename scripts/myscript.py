import language_check
tool = language_check.LanguageTool('en-US')
text = 'A sentence with a error in Anjneshs demo tot he team'
matches = tool.check(text)
print(len(matches))   
print(language_check.correct(text, matches))