#Biblioteca que permite usar o método de requisição
import requests 

def obter_dados_meteorologicos(): #Função que executa a consulta
    endereco = "http://127.0.0.1:8000/v1/forecast"

    parametros = { #Parâmetros obrigatórios para a requisição 
        "latitude": -26.4851,
        "longitude": -49.0713,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "wind_speed_10m"
            ]
        }
    
    resposta = requests.get(endereco, params=parametros, timeout=15) #Variável que faz a requisição

    resposta.raise_for_status() #Exibe o código de status da consulta

    dados = resposta.json() #Variável que recebe a resposta em JSON

    condicoes_atuais = dados["current"] # Acessa a variável junto do parâmetro da requisição

    return{ #Devolve o que foi pedido anteriormente na consulta
        "temperatura": condicoes_atuais["temperature_2m"],   
        "umidade_relativa": condicoes_atuais["relative_humidity_2m"],  
        "sensacao_termica": condicoes_atuais["apparent_temperature"], 
        "precipitacao": condicoes_atuais["precipitation"],
        "velocidade_vento": condicoes_atuais["wind_speed_10m"]
    } 
