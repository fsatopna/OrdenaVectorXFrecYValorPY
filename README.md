
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
* Obtener un vector de pares ordenados con afrec, anum. `{(1,1),(2,3)(1,4)(4,5)}`
* Ordenar el vector de pares por frecuencia y valor. `{1,3,3,4,5,5,5,5}`

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

* ### Ordenar el vector de pares {valor, frecuencia}.
```
afrec = []
for n in anum:
    afrec.append(arr.count(n))

```
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Alternativa de Ordenar el vector de pares {valor, frecuencia}.
```
    sort(mfrec.begin(), mfrec.end(),
         [] (const pair<int,int> &  a, const pair<int,int> &  b) {
             if (a.second == b.second)
                return (a.first < b.first);
            return (a.second < b.second);
             });

```

* ### Obtener la salida desde el vector de pares {valor, frecuencia}.
```

    cout << "resultado: {";
    for(vector<dupla>::iterator it = mfrec.begin();it != mfrec.end(); it++) {
        for (int i=0;i < it->second;i++)
            cout << it->first << ", ";
    }
    cout << "}" << endl;
```


## Notas: 
* ### Modo de ejecución.
La primer linea define una macro de nombre DEBUG, si esta macro se compila con true, muestra información que permite analizar el algoritmo

* ### Alternativa de Implementación.
La segunda linea define una macro de nombre ALTERNATIVA, si esta macro se compila con true, implementa alternativas de ejecución, por ejemplo: cambio de sort de función de relación de orden nominal a anónima(lambda).

```
(base) fsato@fsato-Aspire-E5-475:~/u1/desarrollo/cpp$ grep -n -B 3 ALT *
ordenaFrecyValorcpp.cpp-1-#define DEBUG false
ordenaFrecyValorcpp.cpp:2:#define ALTERNATIVA false 
--
ordenaFrecyValorcpp.cpp-43-
ordenaFrecyValorcpp.cpp-44-    if (arr.size() == 0) return arr;
ordenaFrecyValorcpp.cpp-45-
ordenaFrecyValorcpp.cpp:46:    if (!(ALTERNATIVA)) {
--
ordenaFrecyValorcpp.cpp-51-      );
ordenaFrecyValorcpp.cpp-52-    }
ordenaFrecyValorcpp.cpp-53-
ordenaFrecyValorcpp.cpp:54:    if (ALTERNATIVA) {
--
ordenaFrecyValorcpp.cpp-86-    }
ordenaFrecyValorcpp.cpp-87-    if (DEBUG) cout << "}" << endl;
ordenaFrecyValorcpp.cpp-88-
ordenaFrecyValorcpp.cpp:89:    if (!(ALTERNATIVA)) {
--
ordenaFrecyValorcpp.cpp-97-     if (DEBUG) cout << "}" << endl;
ordenaFrecyValorcpp.cpp-98-    } 
ordenaFrecyValorcpp.cpp-99-
ordenaFrecyValorcpp.cpp:100:    if (ALTERNATIVA) {
```

