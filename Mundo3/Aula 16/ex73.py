times = ('Palmeiras','Palmeiras',
'Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico','Cruzeiro','Botafogo',
'Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG',
'Vitória','Paraná')

Gcinco = times[1:5]
Rebaixados = times[-4:]
chape = times.index('Chapecoense')
alphabetical = sorted(times)

print(f'G cinco: {Gcinco}\nRebaixados: {Rebaixados}\nChapecoense: {chape}\nTimes em ordem alfabética: {alphabetical}')