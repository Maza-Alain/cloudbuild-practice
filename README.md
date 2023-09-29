# crear un artifact registry
gcloud artifacts repositories create cloudbuild-practice-artifacts \
    --repository-format=docker \
    --location=us-central1 \
    --description="artifact repo for cloudbuild-practice" \
    --async

Docu: https://cloud.google.com/artifact-registry/docs/repositories/create-repos?hl=es-419#docker

# crear un repositorio
Este repositorio se conectará a un trigger de cloud build, dentro de este repo deberás incluir tu cloudbuild.yaml y tu código correspondiente, que en este caso se trata de un servidor en python por lo que se necesita un requirements.txt

Tip: Para crear tu requirements.txt puedes utilizar
pip freeze > requirements.txt

# crear un trigger de cloud build
esto lo puedes realizar en consola, solo selecciona Docker y un archivo cloudbuild.yaml. Además obviamente apunta al repo que creamos en el paso anterior


