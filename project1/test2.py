from test import sursa

# def videotext(text, link, audio, output):
#     w = "150"
#     h = "h - 550"
#     os.system(f"""ffmpeg -i {audio} -loop 1 -framerate 10 -i /config/python/videos/back.png -filter_complex \
#         "[1:v]drawtext=text={text}\n\n{link}\n{today}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" -map "[v]" \
#         -map 0:a -c:a copy -movflags +faststart -shortest {output}""")

# videos1 = f"""ffmpeg -i {audio} -loop 1 -framerate 10 -i /config/python/videos/back.png -filter_complex \
#         "[1:v]drawtext=text={text}\n\n{link}\n{today}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         -map "[v]" -map 0:a -c:a copy -movflags +faststart -shortest {output}"""


# videos2 = f"""ffmpeg -i {audio} -i {audio2} -loop 1 -framerate 10 -i /config/python/videos/back.png -filter_complex \
#         "[1:v]drawtext=text={text}\n\n{link}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         "[2:v]drawtext=text={text2}\n\n{link}\n{today}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         -map "[v]" -map 0:a -c:a copy -movflags +faststart -shortest {output}"""

# videos3 = f"""ffmpeg -i {audio} -i {audio2} -i {audio3} -loop 1 -framerate 10 -i /config/python/videos/back.png -filter_complex \
#         "[1:v]drawtext=text={text}\n\n{link}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         "[2:v]drawtext=text={text2}\n\n{link}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         "[3:v]drawtext=text={text3}\n\n{link}\n{today}: fontfile=/config/python/fonts/Kanit-Regular.ttf:fontsize=50:fontcolor=white:x={w}:y={h},format=yuv420p[v]" \
#         -map "[v]" -map 0:a -c:a copy -movflags +faststart -shortest {output}"""


sursed = {'BeInCrypto': beincrypto(link), 'Cointelegraph': cointelegraph(link), 'The Motley Fool': themotleyfool(link), 'FX Street': fxstreet(link), 'CryptoPotato.com': cryptopotato(link), 'Decrypt': decrypt(link), 'ZyCrypto': zycrypto(link), 'Cryptopolitan': cryptopolitan(link),
'BitcoinWorld': bitcoinworld(link), 'CryptoGlobe': cryptoglobe(link), 'CryptoDaily': cryptodaily(link), 'Coingape': coingape(link), 'The Block': theblock(link), 'Bitcoin.com': bitcoincom(link), 'U.Today': utoday(link), 'Legit NG': legitng(link), 'The Punch': thepunch(link), 'DailyCoin': dailycoin(link)}

print(sursed.get(sursa))