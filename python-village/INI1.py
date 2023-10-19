with open('ini1.txt','w') as f:
    import this
    text = "".join([this.d.get(c, c) for c in this.s])
    f.write(text)
