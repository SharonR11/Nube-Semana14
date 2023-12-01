import boto3

def upload_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"Archivo {file_path} subido a {bucket_name} como {object_name}")
    except Exception as e:
        print(f"Error al subir archivo a S3: {e}")

if __name__ == "__main__":
    # Ruta local del archivo de respaldo
    backup_file_path = './backup.sql'
    
    # Nombre del bucket S3 en AWS y nombre del archivo en S3
    s3_bucket_name = 'bucket-nube'
    s3_object_name = 'backup.sql'

    # Llamar a la función para cargar el archivo a S3
    upload_to_s3(backup_file_path, s3_bucket_name, s3_object_name)
