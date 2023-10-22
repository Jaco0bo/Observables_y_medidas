# TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS

En este repositorio encontrara 💻:

## - Un codigo hecho en python con las siguientes funciones 🐍:
- ### SIMULE EL PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4.1.

  - Calcula la probabilidad de encontrar una particula en un sistema en determinada posicion.
  - Si se le da otro vector Ket del sistema de la particula busca la probabilidad de transitar del primer vector al segundo.
 
- ### Complete los retos de programacion del capitulo 4.
  - Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

  - Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

  - El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

  - Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

- ### REALICE LOS SIGUIENTES PROBLEMAS E INCLUYALOS COMO EJEMPLOS:
  - 4.3.1
  - 4.3.2
  - 4.4.1
  - 4.4.2

 Cada ejercicio esta demarcado con un comentario dentro del codigo.

- ### Ejercicios 4.5.2 y 4.5.3
  #### 4.5.2
  Sólo hay dos estados de spin básicos. Para el eje vertical, estos estados son de giro hacia arriba y hacia abajo.

  El estado genérico se describe como: ![image](https://github.com/Jaco0bo/Observables_y_medidas/assets/142515732/5a5903d6-255b-4ca2-bbf7-b59b02940bf1)
  El producto tensorial del espacio vectorial es asociativo. Si hay dos partículas, los estados básicos del espín son:
  ![image](https://github.com/Jaco0bo/Observables_y_medidas/assets/142515732/eda5347e-b236-4a48-883f-99d477e72a6d)
  Para un sistema con n partículas, puedes generalizar esto tomando el producto tensorial de los vectores de estado individuales de todas las n partículas. El vector de estado para el sistema de n partículas es:
  ![image](https://github.com/Jaco0bo/Observables_y_medidas/assets/142515732/def08b3b-3e81-43dd-a355-18c9c0e3bf5e)
  Esto representa el estado de un sistema cuántico con n partículas y puede utilizarse para describir registros cuánticos en la computación cuántica, donde cada qubit en el registro corresponde a una partícula en el sistema.

  #### 4.5.3
  ![image](https://github.com/Jaco0bo/Observables_y_medidas/assets/142515732/8b4c8d8c-e459-4938-b8a2-99a4fe4ce578)
  ##### Estado separable:
  Estados que pueden descomponerse en producto tensorial del estado a partir del subsistema constituyente.
  se dice como: ![image](https://github.com/Jaco0bo/Observables_y_medidas/assets/142515732/2770dcd4-970d-436b-98e6-69894aaba925)
  
  Si un estado no es separable significa que el estado es irrompible, a esto se le llama estado entrelazado.

  Con el estado anterior si intentamos factorizar el y1 que esta en ambas partes nos damos cuenta de que no es posible ya que si consideramos |φ⟩ como el producto tensorial de dos estados independientes, |A⟩ y |B⟩, ya que |A⟩ y |B⟩ no pueden ser iguales a |x0⟩ y (|y1⟩ + 
  |x1⟩) ⊗ |y1⟩, respectivamente. Por lo tanto, esta expresión demuestra que |φ⟩ no puede ser factorizado en dos estados independientes |A⟩ y |B⟩, lo que confirma que |φ⟩ es un estado entrelazado.

## - Archivo .gitignore 📄

## Requisitos:
  - libreria Numpy
  - Python
     

  
