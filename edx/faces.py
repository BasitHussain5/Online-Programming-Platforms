def main():
    tex = input()
    output = convert(tex)
    print(output)

def convert(tex):
    tex1 = tex.replace(":)", "🙂")
    tex2 = tex1.replace(":(", "🙁")
    
    return tex2
    
    
main()
