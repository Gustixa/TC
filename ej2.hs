-- Sitio para ejecutarlo https://www.tutorialspoint.com/compile_haskell_online.php

-- Lista de enteros
listaEnteros :: [Int]
listaEnteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

-- Potencia n
n :: Int
n = 2

-- Calcular la potencia n-ésima de cada elemento en la lista usando lambda
resultado :: [Int]
resultado = map (\x -> x ^ n) listaEnteros

-- Mostrar el resultado
main :: IO ()
main = print resultado
