
***
# Ordenar un vector por frecuencia y valor
***
## Problema: 
Se tiene un vector de enteros, y se desea ordenar el mismo por la frecuencia de cada elemento y para la misma frecuencia por el valor del elemento:

* entrada:  {5, 1, 5, 4, 3, 5, 5, 3}    
* salida :  {1, 4, 3, 3, 5, 5, 5, 5} 

### Entrada
<Table>
  <tr>
      <td>Elementos</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
   </tr>
   <tr>
</Table>

### Frecuencias
<Table>
  <tr>
      <td>Elemento</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
   </tr>
   <tr>
    <td>Frecuencia</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
  </tr>
</Table>

## Objetivo
Comprender y utilizar distintos tipos de colecciones para resolución de problemas de conjunto.

***


## Estrategia: 
* Obtener elementos únicos, anum.           `[1,3,4,5]` 
* Obtener las frecuencias de anum, afrec.   `{1,2,1,4]`
* Obtener un vector de pares ordenados con (afrec,anum). `{frecuencia,valor}`{(1,1),(2,3)(1,4)(4,5)}`
* Ordenar el vector de pares por frecuencia y valor. `{1,3,3,4,5,5,5,5}`frecuencia,valor}

## Implementación: 
* ### Obtener elementos unicos, anum.
```
anum = list(set(arr))

```

* ### Obtener las frecuencias, afrec.
```
afrec = []
for n in anum:
    afrec.append(arr.count(n))
```
Notar que el vector anum no necesariamente debe estar ordenado, si debe tener valores únicos(set).

* ### Obtener un vector de pares ordenados con  valor y frecuencia (afrec,anum), anf.
```
anf= list(zip(afrec,anum))
```

* ### Ordenar el vector, anfs.
```
anfs = sorted(anf)
```


### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Alternativa de Ordenar el vector de pares.
```
sorted(anf, cmp=cmp_tuplas)  

anf= list(zip(af def cmp_tuplas(a, b):
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
rec,anum))
```

* ### Generar el vector resultado desde anfs, res.
```
res =  []
for fila in anfs:
#    print(fila[1],'->',fila[0])
    for i in range(fila[0]):
        res.append(fila[1])

```
