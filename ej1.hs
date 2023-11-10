-- Sitio donde se realizaron las pruebas https://www.tutorialspoint.com/compile_haskell_online.php

import Data.List


[("product","Laptop"), ("price","1000"), ("color","Silver")],
  [("product","Smartphone"), ("price","800"), ("color","Black")],
  [("product","Tablet"), ("price","500"), ("color","Gold")]
  
-- Lista original de diccionarios
d :: [[(String, String)]]
d = [[("make","Nokia"), ("model","216"), ("color","Black")],
     [("make","Apple"), ("model","2"), ("color","Silver")],
     [("make","Huawei"), ("model","50"), ("color","Gold")],
     [("make","Samsung"), ("model","7"), ("color","Blue")]]

-- Clave para ordenar la lista de diccionarios
keyToSort :: String
keyToSort = "make"

-- Función para obtener el valor de la clave, manejando enteros y cadenas
getValue :: String -> [(String, String)] -> Either Int String
getValue key dict = case key of
  "model" -> Left (read $ snd $ head $ filter (\(k, v) -> k == key) dict)
  _       -> Right (snd $ head $ filter (\(k, v) -> k == key) dict)

-- Función para ordenar la lista de diccionarios por la clave indicada
sortD :: String -> [[(String, String)]] -> [[(String, String)]]
sortD key xs = sortBy (\x y -> compare (getValue key x) (getValue key y)) xs

-- Mostrar la lista ordenada
main :: IO ()
main = print $ sortD keyToSort d
