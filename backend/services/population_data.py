# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    population_data.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imuondo <imuondo@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 19:01:52 by imuondo           #+#    #+#              #
#    Updated: 2026/09/22 19:12:09 by imuondo          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import rasterio

def get_population(lat: float, lon: float, year: int):
	filename = f"data/population/population_{year}.tif"
	
	with rasterio.open(filename) as raster:
		row, col = raster.index(lon, lat)
		population = raster.read(1)[row, col]
		return float(population)

def get_temperature(lat: float, lon: float, year: int):
	filename = f"data/temperature/temperature_{year}.tif"
	
	with rasterio.open(filename) as raster:
		row, col = raster.index(lon, lat)
		temperature = raster.read(1)[row, col]
		return float(temperature)
	

def get_nvdi(lat: float, lon: float, year: int):
	filename = f"data/nvdi/nvdi_{year}.tif"
	
	with rasterio.open(filename) as raster:
		row, col = raster.index(lon, lat)
		nvdi = raster.read(1)[row, col]
		return float(nvdi)
	

def get_precipitation(lat: float, lon: float, year: int):
	filename = f"data/precipitation/precipitation_{year}.tif"
	
	with rasterio.open(filename) as raster:
		row, col = raster.index(lon, lat)
		precipitation = raster.read(1)[row, col]
		return float(precipitation)
	
