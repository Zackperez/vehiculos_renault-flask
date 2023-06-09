from flask import Flask, jsonify, request
#from flask_mysqldb import MySQL
import psycopg2
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

#mysql = MySQL(app)

def get_db_connection():
    conn = psycopg2.connect(host='db.elofgzyhnliurwchnmse.supabase.co',
                            database='postgres',
                            port=5432,
                            user='postgres',
                            password='oxHcvidninh5Vh5s')
    return conn

conn = get_db_connection()


@app.route("/insertar_datos/", methods = ['POST'])
def insertar_datos_vehiculo():
    sql = """ INSERT INTO vehiculos_renault (precio, modelo, año, kilometraje) VALUES
('$ 32.000.000', 'SANDERO', '2014', '83.000 km'),
('$ 49.500.000', 'SANDERO', '2017', '54.500 km'),
('$ 60.000.000', 'STEPWAY', '2021', '2.999 km'),
('$ 30.500.000', 'SANDERO', '2011', '125.700 km'),
('$ 16.500.000', 'SANDERO', '2016', '500.000 km'),
('$ 42.000.000', 'SANDERO', '2018', '72.000 km'),
('$ 54.000.000', 'SANDERO', '2022', '15.700 km'),
('$ 52.000.000', 'SANDERO', '2020', '34.000 km'),
('$ 30.000.000', 'SANDERO', '2011', '138.000 km'),
('$ 59.900.000', 'SANDERO', '2022', '7.500 km'),
('$ 69.800.000', 'SANDERO', '2022', '900 km'),
('$ 45.999.999', 'SANDERO', '2022', '28.000 km'),
('$ 46.800.000', 'SANDERO', '2020', '24.000 km'),
('$ 43.500.000', 'SANDERO', '2019', '33.865 km'),
('$ 42.000.000', 'STEPWAY', '2014', '100 km'),
('$ 49.500.000', 'SANDERO', '2020', '31.000 km'),
('$ 55.000.000', 'SANDERO', '2021', '45.000 km'),
('$ 53.000.000', 'SANDERO', '2020', '40.000 km'),
('$ 77.800.000', 'STEPWAY', '2023', '1.550 km'),
('$ 159.900.000', 'ALASKAN', '2022', '18.800 km'),
('$ 50.000.000', 'STEPWAY', '2017', '75.000 km'),
('$ 28.000.000', 'SANDERO', '2012', '159.000 km'),
('$ 34.900.000', 'SANDERO', '2015', '114.000 km'),
('$ 31.900.000', 'SANDERO', '2010', '159.000 km'),
('$ 46.000.000', 'SANDERO', '2019', '40.000 km'),
('$ 36.000.000', 'SANDERO', '2018', '48.000 km'),
('$ 35.000.000', 'SANDERO', '2017', '133.000 km'),
('$ 27.500.000', 'SANDERO', '2010', '163.359 km'),
('$ 28.500.000', 'SANDERO', '2009', '16.333 km'),
('$ 39.000.000', 'SANDERO', '2018', '55.000 km'),
('$ 36.000.000', 'SANDERO', '2015', '120.000 km'),
('$ 40.500.000', 'SANDERO', '2017', '61.000 km'),
('$ 31.900.000', 'SANDERO', '2013', '109.001 km'),
('$ 31.500.000', 'SANDERO', '2011', '153.000 km'),
('$ 34.500.000', 'SANDERO', '2014', '82.100 km'),
('$ 29.900.000', 'SANDERO', '2011', '100.000 km'),
('$ 39.000.000', 'SANDERO', '2017', '53.655 km'),
('$ 31.000.000', 'SANDERO', '2012', '109.000 km'),
('$ 37.000.000', 'SANDERO', '2012', '52 km'),
('$ 40.500.000', 'STEPWAY', '2014', '100.000 km'),
('$ 58.900.000', 'SANDERO', '2022', '16.000 km'),
('$ 61.000.000', 'SANDERO', '2022', '2.300 km'),
('$ 39.500.000', 'SANDERO', '2019', '69.400 km'),
('$ 44.800.000', 'SANDERO', '2019', '48.000 km'),
('$ 49.900.000', 'SANDERO', '2022', '23.000 km'),
('$ 43.000.000', 'SANDERO', '2016', '46.000 km'),
('$ 39.000.000', 'SANDERO', '2016', '78.300 km'),
('$ 53.500.000', 'STEPWAY', '2019', '41.050 km'),
('$ 45.900.000', 'STEPWAY', '2017', '78.514 km'),
('$ 37.000.000', 'SANDERO', '2015', '104.000 km'),
('$ 43.500.000', 'SANDERO', '2019', '49.423 km'),
('$ 61.000.000', 'SANDERO', '2022', '0 km'),
('$ 37.900.000', 'SANDERO', '2016', '98.000 km'),
('$ 36.000.000', 'SANDERO', '2016', '86 km'),
('$ 40.900.000', 'SANDERO', '2015', '51.400 km'),
('$ 36.000.000', 'SANDERO', '2017', '86.164 km'),
('$ 40.000.000', 'SANDERO', '2014', '108.462 km'),
('$ 41.000.000', 'SANDERO', '2017', '264.777 km'),
('$ 27.900.000', 'SANDERO', '2010', '108.000 km'),
('$ 30.000.000', 'SANDERO', '2012', '108.000 km'),
('$ 40.000.000', 'SANDERO', '2018', '90.000 km'),
('$ 53.500.000', 'SANDERO', '2021', '33.000 km'),
('$ 44.000.000', 'SANDERO', '2017', '99.000 km'),
('$ 31.500.000', 'SANDERO', '2010', '72.000 km'),
('$ 31.500.000', 'SANDERO', '2011', '71.000 km'),
('$ 51.900.000', 'STEPWAY', '2018', '48.800 km'),
('$ 30.500.000', 'SANDERO', '2013', '78.000 km'),
('$ 44.500.000', 'SANDERO', '2019', '41.000 km'),
('$ 58.900.000', 'SANDERO', '2021', '36.000 km'),
('$ 27.800.000', 'SANDERO', '2010', '137.000 km'),
('$ 45.000.000', 'SANDERO', '2019', '79.999 km'),
('$ 26.500.000', 'SANDERO', '2010', '165.000 km'),
('$ 35.500.000', 'STEPWAY', '2012', '133.600 km'),
('$ 48.000.000', 'SANDERO', '2019', '4.290 km'),
('$ 32.000.000', 'SANDERO', '2012', '29.400 km'),
('$ 36.500.000', 'SANDERO', '2016', '61.000 km'),
('$ 39.000.000', 'SANDERO', '2016', '74.000 km'),
('$ 36.500.000', 'STEPWAY', '2011', '128.000 km'),
('$ 47.500.000', 'SANDERO', '2021', '20.000 km'),
('$ 39.900.000', 'SANDERO', '2018', '61.000 km'),
('$ 60.000.000', 'SANDERO', '2022', '23.850 km'),
('$ 27.900.000', 'SANDERO', '2011', '40.000 km'),
('$ 31.000.000', 'SANDERO', '2016', '130.000 km'),
('$ 65.000.000', 'SANDERO', '2022', '22.000 km'),
('$ 30.700.000', 'SANDERO', '2013', '100.000 km'),
('$ 38.500.000', 'SANDERO', '2015', '5.830 km'),
('$ 49.000.000', 'SANDERO', '2018', '7.594 km'),
('$ 40.500.000', 'SANDERO', '2016', '75.000 km'),
('$ 27.900.000', 'SANDERO', '2009', '157.000 km'),
('$ 43.500.000', 'SANDERO', '2018', '121.000 km'),
('$ 34.000.000', 'SANDERO', '2015', '77.000 km'),
('$ 46.000.000', 'SANDERO', '2020', '43.000 km'),
('$ 41.000.000', 'SANDERO', '2019', '46.499 km'),
('$ 44.000.000', 'SANDERO', '2018', '48.999 km'),
('$ 46.000.000', 'SANDERO', '2021', '21.000 km'),
('$ 47.000.000', 'SANDERO', '2020', '47.000 km'),
('$ 30.000.000', 'SANDERO', '2012', '82.000 km'),
('$ 62.000.000', 'SANDERO', '2022', '75 km'),
('$ 42.600.000', 'SANDERO', '2018', '60.000 km'),
('$ 54.000.000', 'SANDERO', '2021', '12.000 km'),
('$ 39.900.000', 'SANDERO', '2017', '48.000 km'),
('$ 46.500.000', 'SANDERO', '2017', '18.647 km'),
('$ 57.900.000', 'SANDERO', '2019', '40.000 km'),
('$ 45.000.000', 'SANDERO', '2017', '370.000 km'),
('$ 43.000.000', 'SANDERO', '2020', '38.000 km'),
('$ 44.000.000', 'SANDERO', '2020', '45.000 km'),
('$ 32.000.000', 'SANDERO', '2014', '160.000 km'),
('$ 41.500.000', 'SANDERO', '2019', '48.000 km'),
('$ 55.900.000', 'SANDERO', '2020', '51.000 km'),
('$ 39.900.000', 'SANDERO', '2018', '54.000 km'),
('$ 31.900.000', 'LOGAN', '2012', '116.000 km'),
('$ 26.000.000', 'SANDERO', '2009', '170 km'),
('$ 47.000.000', 'SANDERO', '2019', '45.000 km'),
('$ 51.000.000', 'SANDERO', '2022', '34.000 km'),
('$ 29.000.000', 'SANDERO', '2012', '123 km'),
('$ 33.000.000', 'SANDERO', '2012', '1.598 km'),
('$ 45.900.000', 'SANDERO', '2019', '36.000 km'),
('$ 25.800.000', 'SANDERO', '2010', '141.000 km'),
('$ 34.000.000', 'SANDERO', '2013', '112.000 km'),
('$ 29.900.000', 'SANDERO', '2011', '99.000 km'),
('$ 45.500.000', 'SANDERO', '2020', '43.000 km'),
('$ 49.490.000', 'SANDERO', '2020', '19.600 km'),
('$ 30.500.000', 'SANDERO', '2011', '99.999 km'),
('$ 41.000.000', 'SANDERO', '2017', '68.000 km'),
('$ 37.500.000', 'SANDERO', '2016', '184.000 km'),
('$ 40.000.000', 'SANDERO', '2018', '25.000 km'),
('$ 41.000.000', 'SANDERO', '2018', '85.000 km'),
('$ 45.900.000', 'SANDERO', '2018', '53.000 km'),
('$ 52.900.000', 'SANDERO', '2022', '21.000 km'),
('$ 30.000.000', 'SANDERO', '2013', '124.719 km'),
('$ 34.000.000', 'SANDERO', '2014', '128.490 km'),
('$ 40.000.000', 'SANDERO', '2017', '52.000 km'),
('$ 36.900.000', 'SANDERO', '2019', '144.000 km'),
('$ 43.000.000', 'SANDERO', '2018', '52.500 km'),
('$ 26.000.000', 'SANDERO', '2012', '186.000 km'),
('$ 48.700.000', 'SANDERO', '2021', '15.000 km'),
('$ 33.900.000', 'SANDERO', '2013', '92.427 km'),
('$ 58.000.000', 'STEPWAY', '2019', '38.000 km'),
('$ 35.000.000', 'SANDERO', '2017', '90.000 km'),
('$ 32.000.000', 'SANDERO', '2011', '146.000 km'),
('$ 47.500.000', 'SANDERO', '2017', '56.900 km'),
('$ 43.800.000', 'SANDERO', '2019', '34.692 km'),
('$ 32.000.000', 'SANDERO', '2013', '145 km'),
('$ 53.000.000', 'SANDERO', '2021', '17.000 km'),
('$ 28.500.000', 'SANDERO', '2011', '137.000 km'),
('$ 38.900.000', 'SANDERO', '2016', '56.000 km'),
('$ 30.000.000', 'SANDERO', '2012', '125.000 km'),
('$ 1.000.000', 'SANDERO', '2015', '53.000 km'),
('$ 26.000.000', 'SANDERO', '2010', '216.500 km'),
('$ 1.000.000', 'SANDERO', '2017', '40.000 km'),
('$ 26.500.000', 'SANDERO', '2010', '110.000 km'),
('$ 48.900.000', 'STEPWAY', '2018', '48.000 km'),
('$ 27.900.000', 'SANDERO', '2009', '158 km'),
('$ 43.500.000', 'SANDERO', '2019', '57.300 km'),
('$ 27.000.000', 'SANDERO', '2009', '107.000 km'),
('$ 45.000.000', 'SANDERO', '2017', '85.000 km'),
('$ 1.000.000', 'SANDERO', '2021', '18.000 km'),
('$ 38.000.000', 'SANDERO', '2018', '65.000 km'),
('$ 35.000.000', 'STEPWAY', '2012', '86.199 km'),
('$ 29.900.000', 'STEPWAY', '2010', '114.000 km'),
('$ 36.700.000', 'SANDERO', '2015', '64.500 km'),
('$ 44.800.000', 'SANDERO', '2018', '13.450 km'),
('$ 41.000.000', 'SANDERO', '2018', '80.000 km'),
('$ 54.000.000', 'SANDERO', '2019', '30.000 km'),
('$ 27.000.000', 'SANDERO', '2010', '127.000 km'),
('$ 65.000.000', 'SANDERO', '2020', '25.000 km'),
('$ 32.000.000', 'SANDERO', '2012', '174.100 km'),
('$ 28.000.000', 'SANDERO', '2012', '119.000 km'),
('$ 33.000.000', 'SANDERO', '2014', '80.000 km'),
('$ 67.900.000', 'STEPWAY', '2022', '27.000 km'),
('$ 52.000.000', 'SOUL', '2015', '59.000 km'),
('$ 30.900.000', 'SANDERO', '2012', '127.000 km'),
('$ 46.000.000', 'SANDERO', '2019', '40.500 km'),
('$ 33.500.000', 'SANDERO', '2015', '143.000 km'),
('$ 37.000.000', 'STEPWAY', '2012', '132.000 km'),
('$ 49.800.000', 'SANDERO', '2020', '11.800 km'),
('$ 25.500.000', 'SANDERO', '2010', '145.000 km'),
('$ 60.000.000', 'SANDERO', '2019', '64.000 km'),
('$ 28.900.000', 'SANDERO', '2012', '143.997 km'),
('$ 30.990.000', 'SANDERO', '2012', '77.300 km'),
('$ 31.500.000', 'SANDERO', '2013', '105.000 km'),
('$ 45.000.000', 'SANDERO', '2019', '25.712 km'),
('$ 34.800.000', 'SANDERO', '2015', '134.496 km'),
('$ 30.000.000', 'SANDERO', '2012', '113.336 km'),
('$ 57.000.000', 'SANDERO', '2022', '11.800 km'),
('$ 69.900.000', 'SANDERO', '2022', '900 km'),
('$ 38.500.000', 'SANDERO', '2017', '104.000 km'),
('$ 52.000.000', 'STEPWAY', '2017', '49.000 km'),
('$ 28.000.000', 'SANDERO', '2010', '135.000 km'),
('$ 73.000.000', 'STEPWAY', '2022', '20.000 km'),
('$ 32.000.000', 'SANDERO', '2014', '95.500 km'),
('$ 55.000.000', 'SANDERO', '2022', '13.000 km'),
('$ 62.900.000', 'STEPWAY', '2020', '44.000 km'),
('$ 37.000.000', 'SANDERO', '2015', '120 km'),
('$ 38.900.000', 'SANDERO', '2016', '101.000 km'),
('$ 39.000.000', 'STEPWAY', '2012', '70.000 km'),
('$ 34.800.000', 'SANDERO', '2013', '92.000 km'),
('$ 31.000.000', 'STEPWAY', '2011', '137.000 km'),
('$ 74.100.000', 'SANDERO', '2022', '0 km'),
('$ 58.500.000', 'SANDERO', '2022', '7.000 km'),
('$ 37.000.000', 'SANDERO', '2015', '80.000 km'),
('$ 52.000.000', 'STEPWAY', '2018', '80.000 km'),
('$ 26.900.000', 'SANDERO', '2010', '110.000 km'),
('$ 44.500.000', 'SANDERO', '2020', '36.500 km'),
('$ 41.000.000', 'SANDERO', '2016', '110.000 km'),
('$ 31.100.000', 'SANDERO', '2012', '78.300 km'),
('$ 33.500.000', 'SANDERO', '2013', '73.000 km'),
('$ 58.500.000', 'SANDERO', '2022', '11.750 km'),
('$ 50.990.000', 'SANDERO', '2018', '32.600 km'),
('$ 30.000.000', 'SANDERO', '2012', '132.800 km'),
('$ 33.000.000', 'SANDERO', '2013', '154.000 km'),
('$ 28.000.000', 'SANDERO', '2011', '109.000 km'),
('$ 41.900.000', 'SANDERO', '2017', '50.000 km'),
('$ 38.500.000', 'SANDERO', '2017', '0 km'),
('$ 31.800.000', 'SANDERO', '2011', '91.300 km'),
('$ 36.500.000', 'SANDERO', '2014', '144.000 km'),
('$ 45.000.000', 'SANDERO', '2018', '30.000 km'),
('$ 38.000.000', 'SANDERO', '2017', '85.800 km'),
('$ 40.000.000', 'SOUL', '2018', '57 km'),
('$ 30.800.000', 'SANDERO', '2014', '121.000 km'),
('$ 41.900.000', 'SANDERO', '2020', '22.996 km'),
('$ 33.800.000', 'SANDERO', '2012', '35.000 km'),
('$ 38.550.000', 'SANDERO', '2017', '62.000 km'),
('$ 23.000.000', 'SANDERO', '2012', '157.000 km'),
('$ 47.800.000', 'SANDERO', '2020', '8.200 km'),
('$ 27.000.000', 'SANDERO', '2010', '133.684 km'),
('$ 51.900.000', 'SANDERO', '2018', '40.117 km'),
('$ 37.000.000', 'SANDERO', '2015', '71.400 km'),
('$ 35.000.000', 'SANDERO', '2016', '115.000 km'),
('$ 43.000.000', 'SANDERO', '2016', '80.000 km'),
('$ 47.990.000', 'SANDERO', '2018', '37.306 km'),
('$ 33.800.000', 'STEPWAY', '2012', '87 km'),
('$ 35.500.000', 'SANDERO', '2018', '117.000 km'),
('$ 34.500.000', 'SANDERO', '2013', '107.777 km'),
('$ 49.500.000', 'SANDERO', '2020', '31.311 km'),
('$ 39.900.000', 'SANDERO', '2018', '80.999 km'),
('$ 31.000.000', 'SANDERO', '2012', '68 km'),
('$ 34.000.000', 'SANDERO', '2015', '45.000 km'),
('$ 43.000.000', 'SANDERO', '2018', '87.500 km'),
('$ 32.900.000', 'SANDERO', '2014', '109.573 km'),
('$ 31.500.000', 'SANDERO', '2011', '71.000 km'),
('$ 34.500.000', 'SANDERO', '2012', '77.700 km'),
('$ 50.900.000', 'SANDERO', '2021', '31.000 km'),
('$ 46.500.000', 'SANDERO', '2016', '104.000 km'),
('$ 41.900.000', 'SANDERO', '2019', '49.000 km'),
('$ 53.000.000', 'SANDERO', '2021', '17.000 km'),
('$ 32.000.000', 'STEPWAY', '2010', '110.000 km'),
('$ 61.500.000', 'STEPWAY', '2022', '22.333 km'),
('$ 34.500.000', 'SANDERO', '2013', '90.000 km'),
('$ 42.000.000', 'STEPWAY', '2015', '111.416 km'),
('$ 42.000.000', 'SANDERO', '2018', '54.700 km'),
('$ 27.500.000', 'SANDERO', '2010', '180.523 km'),
('$ 65.000.000', 'SANDERO', '2022', '7.500 km'),
('$ 27.000.000', 'SANDERO', '2010', '65.000 km'),
('$ 28.000.000', 'SANDERO', '2012', '142.000 km'),
('$ 52.000.000', 'SANDERO', '2021', '27.000 km'),
('$ 46.000.000', 'SANDERO', '2020', '25.100 km'),
('$ 47.000.000', 'SANDERO', '2020', '55.000 km'),
('$ 35.800.000', 'SANDERO', '2015', '89.000 km'),
('$ 31.000.000', 'SANDERO', '2013', '97.500 km'),
('$ 34.000.000', 'SANDERO', '2012', '156.700 km'),
('$ 31.800.000', 'SANDERO', '2012', '116.000 km'),
('$ 53.000.000', 'SANDERO', '2019', '47.000 km'),
('$ 27.000.000', 'STEPWAY', '2011', '251.000 km'),
('$ 26.500.000', 'SANDERO', '2011', '95.000 km'),
('$ 38.500.000', 'SANDERO', '2016', '86.800 km'),
('$ 28.000.000', 'SANDERO', '2013', '110.000 km'),
('$ 31.000.000', 'SANDERO', '2012', '89.000 km'),
('$ 68.500.000', 'STEPWAY', '2022', '12.000 km'),
('$ 42.500.000', 'SANDERO', '2018', '58.000 km'),
('$ 31.900.000', 'SANDERO', '2013', '92.000 km'),
('$ 35.500.000', 'SANDERO', '2016', '1.234 km'),
('$ 44.000.000', 'SANDERO', '2019', '30.000 km'),
('$ 28.900.000', 'SANDERO', '2012', '144 km'),
('$ 32.900.000', 'SANDERO', '2014', '83.000 km'),
('$ 27.500.000', 'SANDERO', '2012', '97.050 km'),
('$ 40.000.000', 'SANDERO', '2017', '105.000 km'),
('$ 44.000.000', 'SANDERO', '2021', '26.741 km'),
('$ 39.800.000', 'SANDERO', '2019', '74.000 km'),
('$ 42.000.000', 'SANDERO', '2019', '35.000 km'),
('$ 43.000.000', 'SANDERO', '2019', '69.000 km'),
('$ 62.900.000', 'SANDERO', '2022', '10.000 km'),
('$ 29.000.000', 'SANDERO', '2011', '140.000 km'),
('$ 38.500.000', 'SANDERO', '2017', '89.000 km'),
('$ 44.200.000', 'SANDERO', '2018', '49.348 km'),
('$ 26.000.000', 'SANDERO', '2012', '120.000 km'),
('$ 46.000.000', 'SANDERO', '2019', '55.020 km'),
('$ 43.000.000', 'SANDERO', '2020', '32.300 km'),
('$ 31.500.000', 'SANDERO', '2012', '88.500 km'),
('$ 54.500.000', 'SANDERO', '2022', '2.300 km'),
('$ 44.500.000', 'SANDERO', '2019', '62.000 km'),
('$ 38.000.000', 'SANDERO', '2018', '95.800 km'),
('$ 27.000.000', 'SANDERO', '2011', '105.000 km'),
('$ 40.000.000', 'SANDERO', '2017', '60.000 km'),
('$ 40.500.000', 'SANDERO', '2018', '68.000 km'),
('$ 32.500.000', 'SANDERO', '2015', '72.000 km'),
('$ 37.500.000', 'SANDERO', '2014', '139.000 km'),
('$ 39.000.000', 'SANDERO', '2016', '95.300 km'),
('$ 35.000.000', 'STEPWAY', '2011', '145.000 km'),
('$ 48.000.000', 'SANDERO', '2021', '23.000 km'),
('$ 50.000.000', 'STEPWAY', '2018', '0 km'),
('$ 46.000.000', 'SANDERO', '2021', '17.000 km'),
('$ 26.500.000', 'SANDERO', '2010', '112.000 km'),
('$ 28.000.000', 'SANDERO', '2016', '100.000 km'),
('$ 52.000.000', 'STEPWAY', '2017', '39.000 km'),
('$ 49.000.000', 'SANDERO', '2021', '56.700 km'),
('$ 31.300.000', 'SANDERO', '2011', '140.000 km'),
('$ 29.000.000', 'SANDERO', '2010', '222.180 km'),
('$ 59.000.000', 'SANDERO', '2022', '6.000 km'),
('$ 28.900.000', 'SANDERO', '2012', '160.000 km'),
('$ 40.000.000', 'SANDERO', '2019', '53.000 km'),
('$ 42.500.000', 'SANDERO', '2018', '45.000 km'),
('$ 40.300.000', 'SANDERO', '2016', '87.000 km'),
('$ 29.000.000', 'SANDERO', '2012', '140.000 km'),
('$ 60.000.000', 'SANDERO', '2022', '10.000 km'),
('$ 38.500.000', 'SANDERO', '2016', '56.000 km'),
('$ 47.500.000', 'SANDERO', '2021', '23.000 km'),
('$ 56.500.000', 'STEPWAY', '2019', '43.000 km'),
('$ 60.000.000', 'SANDERO', '2022', '25.000 km'),
('$ 34.300.000', 'SANDERO', '2015', '99.800 km'),
('$ 51.000.000', 'SANDERO', '2021', '18.500 km'),
('$ 40.700.000', 'KWID', '2020', '27.000 km'),
('$ 42.700.000', 'KWID', '2021', '11.000 km'),
('$ 62.000.000', 'SANDERO', '2022', '8.500 km'),
('$ 46.500.000', 'SANDERO', '2020', '68.000 km'),
('$ 47.000.000', 'STEPWAY', '2017', '64.400 km'),
('$ 47.900.000', 'SANDERO', '2021', '22.000 km'),
('$ 37.900.000', 'STEPWAY', '2013', '87.500 km'),
('$ 37.900.000', 'STEPWAY', '2013', '87.000 km'),
('$ 26.000.000', 'SANDERO', '2011', '139.000 km'),
('$ 48.500.000', 'SANDERO', '2022', '38.000 km'),
('$ 49.500.000', 'SANDERO', '2021', '18.000 km'),
('$ 48.990.000', 'SANDERO', '2020', '8.500 km'),
('$ 22.000.000', 'KWID', '2016', '55.000 km'),
('$ 23.000.000', 'KWID', '2015', '23.000 km'),
('$ 35.000.000', 'LOGAN', '2017', '25.000 km'),
('$ 45.000.000', 'LOGAN', '2021', '5.000 km'),
('$ 35.000.000', 'LOGAN', '2018', '155.000 km'),
('$ 25.000.000', 'ALASKAN', '2015', '10.000 km'),
('$ 55.000.000', 'ALASKAN', '2018', '0 km'),
('$ 55.000.000', 'ALASKAN', '2021', '10.000 km'),
('$ 50.000.000', 'LOGAN', '2015', '25.000 km') """
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()
    print("Datos añadidos a la BD ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})

@app.route('/mostrar_registros/', methods=['GET'])
def registrar_db():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehiculos_renault')
    registros = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]
    resultado = []
    for registro in registros:
        resultado.append(dict(zip(columnas, registro)))
    insertar_datos_vehiculo(resultado[0])
    return jsonify(resultado)

@app.route("/modificar_datos_vehiculo", methods=['POST'])
def modificar_datos_vehiculo():

    datos_vehiculo = {
        'modificar_id': request.json['modificarId'],
        'modificar_kilometraje': request.json['modificarKilometraje'],
        'modificar_precio': request.json['modificarPrecio']
    }

    id = datos_vehiculo['modificar_id']
    kilometraje = datos_vehiculo['modificar_kilometraje']
    precio = datos_vehiculo['modificar_precio']

    cur = conn.cursor()
    sql = ("UPDATE vehiculos_renault SET precio = %s, kilometraje = %s WHERE id = %s")
    val = (precio, kilometraje, id)
    cur.execute(sql,val)
    cur.close()
    conn.commit()
    print("Modificación realizada ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})

@app.route("/eliminar_datos_vehiculo/<id>", methods=['DELETE'])
def eliminar_datos_vehiculo(id):
    print(id)
    cur = conn.cursor()

    sql = ("DELETE FROM vehiculos_renault WHERE id = %s")
    val = (id,)
    cur.execute(sql,val)
    cur.close()
    conn.commit()
    print("eliminación realizada ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})

@app.route('/consultar_datos_vehiculo/<id>', methods=['GET'])
def consultar_datos_vehiculo(id):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM vehiculos_renault WHERE id = %s', [id])
        rv = cur.fetchall()
        cur.close()
        return jsonify(rv)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/iniciar_sesion', methods = ['POST'])
def iniciar_sesion():

    datos_usuario = {
        'usuario': request.json['correo'],
        'contrasena': request.json['contrasena']
    }

    usuario = datos_usuario['usuario']
    contrasena = datos_usuario['contrasena']

    cursor = conn.cursor()
    cursor.execute('SELECT usuario, contrasena FROM usuario WHERE usuario LIKE %s and contrasena = %s', (usuario, contrasena))
    registro = cursor.fetchall()
    return jsonify(len(registro))

#Mostrar los registros de la BD en la tabla
@app.route('/mostrar_registros_tabla/', methods=['GET'])
def mostrar_registros_tabla():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehiculos_renault')
    registros = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]
    resultado = []
    for registro in registros:
        resultado.append(dict(zip(columnas, registro)))
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug = True, port = 4000)