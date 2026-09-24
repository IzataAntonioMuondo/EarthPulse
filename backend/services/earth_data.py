# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    earth_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imuondo <imuondo@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 18:19:37 by imuondo           #+#    #+#              #
#    Updated: 2026/09/22 19:28:02 by imuondo          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import FastAPI
from population_data import get_population, get_nvdi, get_precipitation, get_temperature

app = FastAPI()

@app.get("/api/earth-data")

def	get_earth_data(lat: float, lon: float, year: int):
    population = get_population(lat, lon, year)
    temperature = get_temperature(lat, lon, year)
    nvdi = get_nvdi(lat, lon, year)
    precipitation = get_precipitation(lat, lon, year)
    print("Teste")
    return {
        "population" : population,
        "temperature" : temperature,
        "nvdi" : nvdi,
        "precipitation" : precipitation,
    }

get_earth_data(-8.34,13.32,2025)
