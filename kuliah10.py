import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("pertemuan 10: interaksi streamlit dan yahoo finance")

kamus_ticker = {
    "GOOGL": 'Google',
    'APPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDanoald's Corp",
    'META': "Meta Platfroms Inc",
    'TLKM.JK': "Telkom Indonesia (Persero) Tbk PT",
    'BBNI.JK': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nesle 5A',
    'GP': 'Perusahaan Gia'
}

ticker_symbol = st.selectbox(
    'silahkan pilih perusahaan:',
    sorted(kamus_ticker.keys() )
)

st.write(kamus_ticker[ticker_symbol])

ticker_data = yf.Ticker(ticker_symbol)
pilihan_periode =st.selectbox(
    'pilih periode:',
    ['1d','5d','2mo','5mo','1y','5y']
)
tgl_mulai = st.date_input(
    'mulai tanggal',
    value=date.today()
)
tgl_akhir=st.date_input(
    'sampel tanggal',
    value=date.today()
)
st.write(f'tanggal mulai:{tgl_mulai}')
st.write(f'tanggal akhir:{tgl_akhir}')

df_ticker=ticker_data.history(
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('tampilkan tabel')

if pilihan_tampil_tabel == True:
    st.write("## lima data awal")
    st.write(df_ticker.head() )

st.write(f"## visualisasi pergerakan saham {kamus_ticker[ticker_symbol]}")

pilihan_atribut= st.multiselect(
    'silahkan pilih atribut yang akan di tampilkan:',
    ['Low','High','Open','Close','Volume']
)

grafik=px.line(
    df_ticker,
    y=pilihan_atribut,
    title=f"harga saham {kamus_ticker[ticker_symbol]}"
)
st.plotly_chart(grafik)

st.write()

https://share.streamlit.io/
https://github.com/
https://share.streamlit.io/user/giazhulaika-ai