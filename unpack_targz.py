import shutil, logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = 'viaje.log',
    filemode = 'w',)
logging.info("Inicio del proceso")
archivo_zip = shutil.make_archive("viaje",
    "zip",
    base_dir ="carpeta-fotos",
    logger=logging)
logging.info("Fin del proceso")