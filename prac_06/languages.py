from prac_06.programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby, visual_basic]

dynamic_languages = [langauge for langauge in languages if langauge.is_dynamic()]
for langauge in dynamic_languages:
    print(langauge.name)

