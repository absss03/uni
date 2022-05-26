#Abigail Barbieri
#barbieriabigailok@gmail.com


#!/usr/bin/bash

fecha=$(date +%y-%m-%d)                 							#se definie la variable donde esta almacenada la fecha						
directorio=$1														#se define al argumento 1 como una variable
archivozip=$directorio-$fecha										#definir la variable donde esta almacenado el nombre del archivo (el cual consta de el argumento ingresado seguido por la fecha) 

test -d $directorio 1>salida 2>errores 								#se prueba si el argumento ingreasado es un directorio o no y se redirige el stdout a un archivo llamado salida y el stderr a un archivo llamado errores

if [ $? -eq 0 ]														#si test -d devuelve 0 significa que $directorio es un directorio
  then
  echo "el directorio es valido" >>salida							#se guarda el mensaje en el arcivo salida
  zip -r $archivozip $directorio 1>>salida 2>>errores				#se crea un zip del directorio ingresado
  if [ $? -eq 0 ]													#si el comando zip devuelve 0 significa que se creo sin ningun problema
    then 
    echo "se creo el backup" $archivozip >>salida					#se guarda el mensaje en el arcivo salida
    zip -q -u $archivozip salida									#se agrega (-u) el archivo salida al zip (-q no es estrictamnete necesario pero queda mas prolijo cuando se ejecuta el script)
  else 																#si el comando zip devuelve otra cosa significa ocurrio algun error al intentar hacerse el zip
    echo "fallo la creacion del backup" $archivozip >>errores		#se guarda el mensaje en el arcivo errores
    zip -q -u _$archivozip salida errores							#se agrega el archivo errores al zip
  fi
  exit
else 																#si test -d devuelve otra cosa significa que $directorio no es un directorio
  echo "el directorio no es valido"	>>errores						#se guarda el mensaje en el arcivo errores
  zip -q -u _$archivozip errores									#se agrega el archivo errores al zip						
fi