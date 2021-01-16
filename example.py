from comment_header_creator import uniline, multiline, generate_line

print("uniline() no passed title:")
print(uniline())
print("\nuniline() passed title:")
print(uniline(title='asdfasdf'))

print("\nmultiline() no passed title:")
print(multiline())
print("\nmultiline() passed title:")
print(multiline(title='asdfasdf'))


print("\nCall the generator directly.  (Remember it returns a Tuple!)")
output, status = generate_line(title='ASDf')
print(f"{output}")
output, status = generate_line()
print(f"\n{output}")
