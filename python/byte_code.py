import dis
piece_of_code = "s[s] += b"
print(f'show byte code for python : {piece_of_code}')
print(dis.dis(piece_of_code))
