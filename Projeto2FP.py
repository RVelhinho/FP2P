#Tipos Abstratos de Dados

#1.Construtor:
def faz_pos(l,c): 
      if isinstance(l,int)==False or isinstance(c,int)==False or l<0 or c<0: #Verificacao dos argumentos
            raise ValueError('faz_pos: argumentos errados')
      else:
            return (l,c)
      
#2.Seletores:
def linha_pos(p):
      return p[0]  #Vai retornar o primeiro elemento que corresponde a linha
      
def coluna_pos(p):
      return p[1]  #Vai retornar o segundo elemento que corresponde a coluna

#3.Reconhecedores:
def e_pos(arg):
      if isinstance(arg,tuple) and len(arg)==2 and arg[0]>=0 and arg[1]>=0 and isinstance(arg[0],int) and isinstance(arg[1],int):
            return True
      else:
            return False
      
#4.Testes:
def pos_iguais(p1,p2):
      if linha_pos(p1)==linha_pos(p2) and coluna_pos(p1)==coluna_pos(p2): #Caso as linhas e as colunas sejam iguais
            return True
      else:
            return False


#Tipo chave:

#1.Construtores:
#Chave em Linha:
#Alfabeto=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')   

def ver_letras_presente(l,mgc):
      for i1 in mgc:
            if i1 == ' ':
                  lst += ''
            elif i1 not in l:
                  raise ValueError ('gera_chave_linhas: argumentos errados')
            else:
                  return True #Verifica se ha alguma letra na mgc que nao pertenca ao conjunto l
            
def ver_letras_iguais(l,mgc):
      alfabeto=[]
      for j in l:
            if j not in alfabeto:
                  alfabeto += [j]
            if len(alfabeto)!= 25:
                  raise ValueError('gera_chave_linhas: argumentos errados') # Permite verificar se existem letras iguais no conjunto l 
            else:
                  return True
            
def gera_chave_linhas(l,mgc):
      if isinstance(l,tuple)==False or len(l)<25 or isinstance(mgc,str)==False: #Verificacao dos argumentos
            raise ValueError('gera_chave_linhas: argumentos errados')
      if ver_letras_presente and ver_letras_iguais:
            lst=[]
            res={}
            alfabeto=[]
            for j in l:
                  if j not in alfabeto:
                        alfabeto += [j]
            if len(alfabeto)!= 25:
                  raise ValueError('gera_chave_linhas: argumentos errados') # Permite verificar se existem letras iguais no conjunto l
            
            for i in range(len(mgc)):
                  if mgc[i]==' ':
                        lst+=''
                  elif mgc[i] not in l:
                        raise ValueError('gera_chave_linhas: argumentos errados')
                  elif mgc[i] not in res and mgc[i]!=' ':
                        res[mgc[i]]=1
                        lst+=[mgc[i]]           #Adiciona cada letra presente em mgc a lista
            for j2 in l:
                  if isinstance(j2,str) == False:
                        raise ValueError ('gera_chave_linhas: argumentos errados')
                  if j2 not in res:  
                        lst+=j2                       #Cada elemento do conjunto l que ainda nao se encontra presente vai ser adicionado a lista
            return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]]          

#Chave em Espiral:
def gera_chave_espiral(l,mgc,s,pos):
      if isinstance(l,tuple)==False or len(l)<25 or isinstance(mgc,str)==False or isinstance(s, str)==False or isinstance(pos,tuple)==False or len(pos)<2: #Verificacao dos argumentos
                  raise ValueError('gera_chave_espiral: argumentos errados')
      lst=[]
      res={}      
      for i in range(len(mgc)):
                  if mgc[i]==' ':
                        lst+='' #Caso a string seja vazia vai apagala
                  elif mgc[i] not in l:
                        raise ValueError('gera_chave_espiral: argumentos errados') #Verifica se todas as letras em mgc estao presentes em l
                  elif mgc[i] not in res and mgc[i]!=' ':
                        res[mgc[i]]=1
                        lst+=[mgc[i]]  # Vai adicionar as letras presentes na mgc      
      for j2 in l:
            if isinstance(j2,str) == False:
                  raise ValueError ('gera_chave_espiral: argumentos errados') # Se os carateres em l nao forem strings gera erro
            if j2 not in res:  
                  lst+=j2     #Vai adicionar as letras presentes no conjunto l que ainda nao estao na lista lst
      if s == 'r':
            if pos == (0,0):
                  lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[15],lst[16],lst[17],lst[18],lst[5],lst[14],lst[23],lst[24],lst[19],lst[6],lst[13],lst[22],lst[21],lst[20],lst[7],lst[12],lst[11],lst[10],lst[9],lst[8]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao do relogio e na primeira linha e primeira coluna
            elif pos == (0,4):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[12],lst[13],lst[14],lst[15],lst[0],lst[11],lst[22],lst[23],lst[16],lst[1],lst[10],lst[21],lst[24],lst[17],lst[2],lst[9],lst[20],lst[19],lst[18],lst[3],lst[8],lst[7],lst[6],lst[5], lst[4]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao do relogio e na primeira linha e ultima coluna
            elif pos == (4,0):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[4],lst[5],lst[6],lst[7],lst[8],lst[3],lst[18],lst[19],lst[20],lst[9],lst[2],lst[17],lst[24],lst[21],lst[10],lst[1],lst[16],lst[23],lst[22],lst[11],lst[0],lst[15],lst[14],lst[13],lst[12]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao do relogio e na ultima linha e primeira coluna
            elif  pos == (4,4):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[8],lst[9],lst[10],lst[11],lst[12],lst[7],lst[20],lst[21],lst[22],lst[13],lst[6],lst[19],lst[24],lst[23],lst[14],lst[5],lst[18],lst[17],lst[16],lst[15],lst[4],lst[3],lst[2],lst[1],lst[0]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao do relogio e na ultima linha e ultima coluna
            else:
                  raise ValueError('gera_chave_espiral: argumentos errados') # Caso os acontecimentos anteriores nao se verifiquem
      elif s == 'c':
            if pos == (0,0):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[0],lst[15],lst[14],lst[13],lst[12],lst[1],lst[16],lst[23],lst[22],lst[11],lst[2],lst[17],lst[24],lst[21],lst[10],lst[3],lst[18],lst[19],lst[20],lst[9],lst[4],lst[5],lst[6],lst[7],lst[8]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao contraria na primeira linha e primeira coluna
            elif pos == (0,4):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[4],lst[3],lst[2],lst[1],lst[0],lst[5],lst[18],lst[17],lst[16],lst[15],lst[6],lst[19],lst[24],lst[23],lst[14],lst[7],lst[20],lst[21],lst[22],lst[13],lst[8],lst[9],lst[10],lst[11],lst[12]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao contraria na primeira linha e ultima coluna
            elif pos == (4,0):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[12],lst[11],lst[10],lst[9],lst[8],lst[13],lst[22],lst[21],lst[20],lst[7],lst[14],lst[23],lst[24],lst[19],lst[6],lst[15],lst[16],lst[17],lst[18],lst[5],lst[0],lst[1],lst[2],lst[3],lst[4]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao contraria na ultima linha e primeira coluna
            elif pos == (4,4):
                  lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12],lst[13],lst[14],lst[15],lst[16],lst[17],lst[18],lst[19],lst[20],lst[21],lst[22],lst[23],lst[24] = lst[8],lst[7],lst[6],lst[5],lst[4],lst[9],lst[20],lst[19],lst[18],lst[3],lst[10],lst[21],lst[24],lst[17],lst[2],lst[11],lst[22],lst[23],lst[16],lst[1],lst[12],lst[13],lst[14],lst[15],lst[0]
                  return [lst[:5],lst[5:10],lst[10:15],lst[15:20],lst[20:]] #Vai alterar letra a letra os valores correspondentes quando esta em direcao contraria na ultima linha e ultima coluna
            else:
                  raise ValueError('gera_chave_espiral: argumentos errados') #Caso os acontecimentos anteriores nao se verifiquem
      else:
            raise ValueError('gera_chave_espiral: argumentos errados')
                  
                  
                  


#2.Seletor:
#Para a chave de linhas:
def ref_chave(c,p):
      return c[p[0]][p[1]] #Vai buscar a letra especifica
         
#3.Modificador:
def muda_chave(c,p,l):
      c[p[0]][p[1]]=l #Altera a letra que esta na posicao do tuplo para a nova letra
      return c
      
#4.Reconhecedores:

def e_chave(arg):
      if isinstance(arg,list)==False or len(arg) != 5:
            return False
      for i in range(len(arg)):
            for j in range(len(arg[i])):
                  if  arg[i][j] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] or isinstance(arg[i][j],str)==False or isinstance(arg[i],list)==False or len(arg[i]) != 5:
                        return False   #Verifica se cada caratere dentro das sublistas correspondente a chave sao strings e se pertencem ao conjunto de letras dada para alem de verificar tambem sobre o comprimento de cada sublista
      else:
            return True
            
#Transformadores:
def string_chave(c):
      string=''
      for i in range(len(c)):
            for j in range(len(c[i])):
                  string+=str(c[i][j]) + ' ' #Existe um espaco entre cada letra
            string+='\n' #Existe um '\n' apos cada sublista da chave
      return string
                        
#Funcoes a desenvolver:

def digramas(mens):
      mens_t=''
      for i in range(len(mens)-1):
                  if mens[i]==' ':
                        mens_t += '' #Caso haja espaco vai eliminar esse espaco
                  elif mens[i] == mens[i+1]:
                        mens_t += mens[i] + 'X' #Se um caratere for igual ao seguinte vai ser adicionado um X
                  else:
                        mens_t += mens[i] #Percorre a mens normalmente
      if len(mens_t)%2 == 0:
            mens_t += mens[-1] + 'X' #Se a len da mens for impar vai adicionar um X 
      elif len(mens_t)%2!=0:
            mens_t += mens[-1] 
      return mens_t

#Auxiliar:

def faz_pos2(letra,chave):
      for i in range(len(chave)):
            for j in range(len(chave[i])):
                  if chave[i][j]==letra:
                        return (i,j) #Vai retornar o tuplo correspondente a letra 


def figura(digrm,chave):
      for i in range(len(digrm)):
            if  coluna_pos(faz_pos2(digrm[0],chave))==coluna_pos(faz_pos2(digrm[1],chave)): #Se a coluna do primeiro caratere for igual a do segundo
                  return ('c',faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))
            elif linha_pos(faz_pos2(digrm[0],chave))==linha_pos(faz_pos2(digrm[1],chave)): #Se a linha do primeiro caratere for igual a do segundo
                  return ('l',faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))
            else:
                  return ('r',faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave)) #Caso contrario
            
def codifica_l(pos1,pos2,inc):
      if inc==1:
            if linha_pos(pos1)==linha_pos(pos2):
                  if coluna_pos(pos1)==4:
                        return ( (linha_pos(pos1),0), (linha_pos(pos2),coluna_pos(pos2)+1))#Se a coluna da primeira posicao for 4 ira passar para 0
                  elif coluna_pos(pos2)==4:
                        return ( (linha_pos(pos1),coluna_pos(pos1)+1), (linha_pos(pos2),0))#Se a coluna da segunda posicao for 4 ira passar para 0   
                  else:
                        return ( (linha_pos(pos1),coluna_pos(pos1)+1), (linha_pos(pos2),coluna_pos(pos2)+1))#Incrementa 1 na coluna de ambas as posicoes
                        
      elif inc==-1:
            if linha_pos(pos1)==linha_pos(pos2):
                  if coluna_pos(pos1)==0:
                        return ( (linha_pos(pos1),4), (linha_pos(pos2),coluna_pos(pos2)-1))#Se a coluna da primeira posicao for 0 ira passar para 4
                  elif coluna_pos(pos2)==0:
                        return ( (linha_pos(pos1),coluna_pos(pos1)-1), (linha_pos(pos2),4))#Se a coluna da primeira posicao for 0 ira passar para 4             
                  else:
                        return ( (linha_pos(pos1),coluna_pos(pos1)-1), (linha_pos(pos2),coluna_pos(pos2)-1))#Decrementa 1 na coluna de ambas as posicoes
def codifica_c(pos1,pos2,inc):
      if inc==1:
            if coluna_pos(pos1)==coluna_pos(pos2):
                  if linha_pos(pos1)==4:
                        return ((0,coluna_pos(pos1)),(linha_pos(pos2)+1,coluna_pos(pos2)))#Se a linha da primeira posicao for 4 ira passar para 0
                  elif linha_pos(pos2)==4:
                        return ((linha_pos(pos1)+1,coluna_pos(pos1)),((0,coluna_pos(pos2))))#Se a linha da segunda posicao for 4 ira passar para 0                                
                  else:
                        return ((linha_pos(pos1)+1,coluna_pos(pos1)),(linha_pos(pos2)+1,coluna_pos(pos2)))#Incrementa 1 na linha de ambas as posicoes           
      elif inc==-1:
            if coluna_pos(pos1)==coluna_pos(pos2):
                  if linha_pos(pos1)==0:
                        return ((4,coluna_pos(pos1)),(linha_pos(pos2)-1,coluna_pos(pos2)))#Se a linha da primeira posicao for 0 ira passar para 4
                  elif linha_pos(pos2)==0:
                        return ((linha_pos(pos1)-1,coluna_pos(pos1)),((4,coluna_pos(pos2))))#Se a linha da segunda posicao for 0 ira passar para 4         
                  else:
                        return ((linha_pos(pos1)-1,coluna_pos(pos1)),(linha_pos(pos2)-1,coluna_pos(pos2)))#Decrementa 1 na linha de ambas as posicoes        
                        
def codifica_r(pos1,pos2):
            return ( (linha_pos(pos1),coluna_pos(pos2)), (linha_pos(pos2),coluna_pos(pos1)))#Devolve a mesma linha mas colunas opostas em cada posicao
      
def codifica_digrama(digrm,chave,inc):
      if inc==1:
            if linha_pos(faz_pos2(digrm[0],chave))==linha_pos(faz_pos2(digrm[1],chave)): #Caso as linhas sejam iguais
                  return ref_chave(chave,codifica_l(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[0])+ref_chave(chave,codifica_l(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[1]) 
            elif coluna_pos(faz_pos2(digrm[0],chave))==coluna_pos(faz_pos2(digrm[1],chave)): #Caso as colunas sejam iguais
                  return ref_chave(chave,codifica_c(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[0])+ref_chave(chave,codifica_c(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[1])
            else:
                  return ref_chave(chave,codifica_r(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))[0])+ref_chave(chave,codifica_r(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))[1])
      elif inc==-1:
            if linha_pos(faz_pos2(digrm[0],chave))==linha_pos(faz_pos2(digrm[1],chave)): #Caso as linhas sejam iguais
                  return ref_chave(chave,codifica_l(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[0])+ref_chave(chave,codifica_l(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[1])
            elif coluna_pos(faz_pos2(digrm[0],chave))==coluna_pos(faz_pos2(digrm[1],chave)): #Caso as linhas sejam iguais
                  return ref_chave(chave,codifica_c(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[0])+ref_chave(chave,codifica_c(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave),inc)[1])
            else:
                  return ref_chave(chave,codifica_r(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))[0])+ref_chave(chave,codifica_r(faz_pos2(digrm[0],chave),faz_pos2(digrm[1],chave))[1])
              
def codifica(mens,chave,inc):
      string=''
      if inc == 1:
            for i in range(0,len(digramas(mens)),2): #Vai percorrer a mens de duas em duas letras
                  string += codifica_digrama(str(digramas(mens)[i]) + str(digramas(mens)[i+1]),chave,inc)  #Vai utilizar a funcao anterior para codificar a mensagem depois de esta ja ter sido modificada pela funcao digramas         
      elif inc == -1:
            for i in range(0,len(mens),2):
                  string += codifica_digrama(str(mens[i])+str(mens[i+1]),chave,inc) #Vai utilizar a funcao anterior para descodificar a mensagem a qual ja se encontra codificada
      return string # Quando acabar de codificar ou descodificar a mens de duas em duas letras vai retornar a mensagem final
