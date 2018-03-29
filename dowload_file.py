import wget

url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv';
filename = wget.download(url)