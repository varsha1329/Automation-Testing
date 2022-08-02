import textwrap
My_text=''' this is my fouth assenment, i am writting this program using python programming  langauge. 
its simple programming langauga and easy to understand, As compare to other langauges.'''
text_remove = textwrap.dedent(My_text)
wrapped = textwrap.fill(text_remove, width = 25)
fin_result=textwrap.indent(wrapped, '> ')
print()
print(fin_result)
print()