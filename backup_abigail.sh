#Abigail Barbieri
#barbieriabigailok@gmail.com

#!/usr/bin/bash					#indica con que programa se ejecuta el script


fecha=$(date +%y-%m-%d)                 #definir la variable donde esta almacenada la fecha
directorio=$1
nombre=$directorio-$fecha						#definir la variable donde esta almacenado el nombre del archivo (el cual consta de el argumento ingresado seguido por la fecha)
  
if test -d $directorio   							#verifica que el argumento ingresado sea efectivamente un directorio
        then										#si es asi procede a: 
            zip -r $nombre $directorio				#crear un archivo.zip que contiene todos los archivos y directorios que se encuentran dentro del directorio(argumento) especificado
			echo "se creo el backup" $nombre		#mostrar un mensaje con el nombre del archivo (en realidad esto es opcional)
        exit 0
else												#si el argumento no es un directorio
    echo "directorio no valido"						#muestra un mensaje
exit 1
 
fi													#finaliza el script
