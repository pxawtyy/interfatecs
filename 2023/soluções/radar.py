velo = int(input()) # 0 <= velo <= 300

if velo <= 107:
    velo_max = velo + 7 # margem de erro: 7km/h se velocidade até 107km/h
else:
    velo_max = round(velo + (velo * 0.07)) # senão, margem de erro: 7% da velocidade (* 0.07) + arrendondamento

print(velo_max)