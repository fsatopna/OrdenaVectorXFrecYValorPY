
def ordenaFrecYValor(arr):
      anum = list(set(arr))
      #print("col1: set nros  : ",anum)
      
      #arr.sort(  )
      #print("entrada ordenada: ",arr)

      afrec = []
      for n in anum:
         afrec.append(arr.count(n))
    
      #print("col2: set frecs : ",afrec)    

      anf= list(zip(afrec,anum))
      #print("pares (frec,num): ",anf)    

      anfs = sorted(anf)
      #print("pares ordenados : ",anfs)

      res =  []
      for fila in anfs:
      #    print(fila[1],'->',fila[0])
         for i in range(fila[0]):
            res.append(fila[1])
        
      return res

'''
 def cmp_tuplas(a, b):
   if a[0]>b[0]:
      return 1
   elif a[0]<b[0]:
      return -1
   else:
       if a[1]<b[1]:
          return 1
       elif a[1]>b[1]:
          return -1
       else:
          return 0
   
sorted(anf, cmp=cmp_tuplas)  # Python2 solo!
     
'''

arr1 =  [5,1,5,4,3,5,5,3]
print("entrada         : ",arr1)

res1 = ordenaFrecYValor(arr1)
print("resultado       : ",res1)

