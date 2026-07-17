#polimorfizm
#
def delete_imports(code, language):
    if language == 'python':
        return code.replace('import ', '')
    elif language == 'SQL':
        return code
    elif language == 'C++':
        return code.replace('#include ', '')
    else:
        return code

def delete_commands(code, language):
    if language == 'python':
        return code.replace('eval', '').replace('exec', '')
    elif language == 'SQL':
        return code.replace('drop', '').replace('delete', '')
    else:
        return code

mycode = """
import os, sys

a = 1
eval(a)
"""
language = 'python'
mycode = delete_commands(mycode, language)
mycode = delete_imports(mycode, language)
print(mycode)



class lexic:
    def __init__(self, code):
        self.code = code

class SQLLexic(lexic):
    def delete_commands(self):
        self.code = self.code.replace('drop', '').replace('delete', '')

    def delete_imports(self):
        ...

    def delete_comments(self):
        self.code = self.code.replace('--', '')

    def process(self):
        self.delete_commands()
        self.delete_comments()

class PythonLexic(lexic):
    def delete_commands(self):
        self.code = self.code.replace('eval', '').replace('exec', '')

    def delete_imports(self):
        self.code = self.code.replace('import ', '')

    def process(self):
        self.delete_commands()
        self.delete_imports()

mycodee = """
import os, sys
--my coment
a = 1
eval(a)
"""
ex = SQLLexic(code=mycodee)
ex.process()
print(ex.code)