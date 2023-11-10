-- Sitio para la ejecucion del programa https://www.tutorialspoint.com/compile_haskell_online.php


["amarillo"]
["amarillo", "blanco"]
["amarillo", "café", "blanco"]
["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]
["morado", "naranja"]


["fruta", "verde", "azul", "rojo", "amarillo", "verde", "fruta", "rojo", "blanco"]
["fruta", "verde", "blanco"]

-- Lista inicial
listaInicial :: [String]
listaInicial = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]

-- Lista de elementos a borrar
elementosABorrar :: [String]
elementosABorrar = ["amarillo", "café", "blanco"]

-- Eliminar elementos indicados usando lambda
listaResultante :: [String]
listaResultante = filter (\x -> not (elem x elementosABorrar)) listaInicial

-- Mostrar el resultado
main :: IO ()
main = print listaResultante
