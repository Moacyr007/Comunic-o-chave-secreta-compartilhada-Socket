def xor(x, y):
    ans = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":
            ans += "1"
        else:
            ans += "0"
    return ans

def convert2Bin(chave, texto):
    if len(chave) == 8:
        return " ".join(f"{ord(i):08b}" for i in texto)
    if len(chave) == 16:
        return " ".join(f"{ord(i):16b}" for i in texto)

def criptografar(chave, chaveBinaria, arquivoBinario):
    
    #separando o arquivo em blocos do tamanho da chave
    if len(chave) == 8:
        
        if(len(arquivoBinario) % len(chaveBinaria) != 0):
            arquivoBinario += ' 00000000'
    elif len(chave) == 16:
        if(len(arquivoBinario) % len(chaveBinaria) != 0):
            arquivoBinario += ' 0000000000000000'
    listaArquivoBinario = arquivoBinario.split()
    listaChaveBinaria = chaveBinaria.split()
    print(listaArquivoBinario)
    print(listaChaveBinaria)

    #efetuando operação XOR entre chave e arquivo
    resultado = ''
    for i in range(0, len(listaArquivoBinario), 2):
        resultado += xor(listaArquivoBinario[i], listaChaveBinaria[0])
        resultado += xor(listaArquivoBinario[i+1], listaChaveBinaria[1])
    
    return resultado

def decriptografar(chave, arquivo, chaveBinaria):

    #separando o arquivo em blocos do tamanho da chave
    listaArquivoBinario = []
    for i in range(0, len(arquivo), 8):
        listaArquivoBinario.append(arquivo[i : i+8])
    listaChaveBinaria = chaveBinaria.split()

    #efetuando operação XOR entre chave e arquivo, convertendo bin para string
    resultado = ''
    for i in range(0, len(listaArquivoBinario), 2):
        resultado += chr(int(xor(listaArquivoBinario[i], listaChaveBinaria[0]), 2))
        resultado += chr(int(xor(listaArquivoBinario[i+1], listaChaveBinaria[1]), 2))
    
    return resultado