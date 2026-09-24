# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    download_data.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: imuondo <imuondo@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 19:46:59 by imuondo           #+#    #+#              #
#    Updated: 2026/09/22 19:52:24 by imuondo          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import rasterio
from rasterio.transform import from_origin
import os
import xarray as xr

os.makedirs("data/population", exist_ok=True)

def obter_dados_da_nasa(ano):

    dataset = xr.open_dataset(
        "data/nasa/population.nc"
    )

    matriz = dataset["population"].sel(
        year=ano
    ).values

    return matriz

for ano in range(2000, 2101):

    caminho = f"data/population/population_{ano}.tif"

    print(f"Processando {ano}...")
    matriz = obter_dados_da_nasa(ano)
    with rasterio.open(
        caminho,
        "w",
        driver="GTiff",
        height=matriz.shape[0],
        width=matriz.shape[1],
        count=1,
        dtype=matriz.dtype,
        crs="EPSG:4326",
        transform=transform
    ) as dst:

        dst.write(matriz, 1)

    print(f"Guardado: {caminho}")