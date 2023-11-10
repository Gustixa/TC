-- Sitio para la ejecucion https://www.tutorialspoint.com/compile_haskell_online.php

-- Matriz X
x :: [[Int]]
x = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]]

-- Calcular la matriz transpuesta XT usando lambda
xt :: [[Int]]
xt = map (\col -> map (!! col) x) [0..length (head x) - 1]

-- Mostrar el resultado
main :: IO ()
main = mapM_ print xt
