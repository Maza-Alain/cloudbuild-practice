# Utiliza la imagen base oficial de MySQL
FROM mysql:latest
# Copia el archivo de configuración personalizado
COPY my.cnf /etc/mysql/conf.d/
# Variables de entorno para configurar el usuario root y la contraseña (personaliza según tus necesidades)
ENV MYSQL_ROOT_PASSWORD=qwerty123

# Puerto que expondrá el contenedor MySQL
EXPOSE 3306

# Comando predeterminado que se ejecutará al iniciar el contenedor
CMD ["mysqld"]

# docker build -t bd-cloudbuild-practice .
# docker run --name local-bd-cloudbuild-practice -d bd-cloudbuild-practice
# docker exec -i local-bd-cloudbuild-practice mysql -uroot -pqwerty123 < ./db.sql
# docker exec -it local-bd-cloudbuild-practice mysql -uroot -pqwerty123

#GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'qwerty123' WITH GRANT OPTION;
